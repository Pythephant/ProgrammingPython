import poplib, sys
from .mailParser import MailParser
from .mailTool import MailTool, SilentMailTool

#index/server msgnum out of synch test
class DeleteSynchError(Exception):
	pass
class TopNotSupported(Exception):
	pass
class MessageSynchError(Exception):
	pass

class MailFetcher(MailTool):
	def __init__(self, popserver = None, popuser=None, poppasswd=None, hastop = True):
		self.popServer = popserver or 'pop.yeah.net'
		self.popUser = popuser or 'jason_wujiakun@yeah.net'
		self.srvrHasTop = self.hastop
		self.popPassword = poppasswd

	def connect(self):
		'''
		get the password of the User
		connect to the server using User Password
		print welcome message
		'''
		self.trace('Connecting...')
		self.getPassword()
		server = poplib.POP3(self.popserver)
		server.user(self.popServer)
		server.pass_(self.popPassword)
		self.trace(server.getwelcome())
		return server

	def decodeFullText(self, messageBytes):
		'''
		decode the bytes of the message
		if decode the content failed
		try to decode the header only
		'''
		text = None
		charsets = ['ascii','latin1','utf8',sys.getdefaultencoding(),'gbk']
		for charset in charsets:
			try:
				text = [line.decode(charset) for line in messageBytes]
				break
			except (UnicodeError, LookupError):
				pass
		#text == None then just decode the header
		if text is None:
			blankline = messageBytes.index(b'')
			hdrLines = messageBytes[:blankline]
			for charset in charsets:
				try:
					text = [line.decode(charset) for line in hdrLines]
					break
				except UnicodeError:
					pass
			if text is None:
				text = ['From: (sender of unknown Unicode format headers)']
			text += ['','--Sorry: mailtools cannot decode this mail content!--']
		return text

	def downloadMessage(self, msgNum):
		'''
		connect to the server 
		then retrieve the message of the specified msgNum
		decode the message bytes to Unicode
		then return the joined unicode string
		'''
		self.trace('load %s'%msgNum)
		server = self.connect()
		try:
			resp, msgBytes, repz = server.retr(msgNum)
		finally:
			server.quit()
		msgLines = self.decodeFullText(msgBytes)
		return '\n'.join(msgLines)

	def downloadAllHeaders(self, process=None, loadfrom=1):
		pass

	def downloadAllMessages(self, process=None, loadfrom=1):
		pass

	def deleteMessages(self, msgNums, progess=None):
		pass

	def deleteMessagesSafely(self, msgNums, synchHeaders, process=None):
		pass
	
	def checkSynchError(self, synchHeaders):
		pass

	def headersMatch(self, hdrtext1, hdrtext2):
		pass

	def getPassword(self):
		if not self.popPassword:
			self.popPassword = self.askPopPassword()

	def askPopPassword(self):
		assert False, 'Subclass must define method'


class MailFetcherConsole(MailFetcher):
	def askPopPassword(self):
		import getpass
		prompt = 'Password for %s on %s' % (self.popUser, self.popServer)
		return getpass.getpass(prompt)

class SilientMailFetcher(SilentMailTool, MailFetcher):
	pass

