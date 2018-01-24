import poplib, sys
from .mailParser import MailParser
from .mailTool import MailTool, SilentMailTool
#global configure
FETCHLIMIT = None

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
		if self.srvHasTop is False:
			return self.downloadAllMessages(process=porcess, loadfrom=loadfrom)
		else:
			self.trace('downloading headers...')
			fetchlimit = FETCHLIMIT
			server = self.connect()
			try:
				resp, msginfos, respsz = server.list()
				msgCounts = len(msginfos)
				msgSizes = [int(msginfo.split()[1]) for msginfo in msginfos]
				msgHdrs = []
				for i in range(loadfrom, msgCounts+1):
					if process:
						process(i, msgCounts)
					if fetchlimit and (i<=msgCounts-fetchlimit):
						hdrtext = 'Subject: -- mail skipped --\n\n'
						msgHdrs.append(hdrtext)
					else:
						resp, hdrBytes, respsz = server.top(i, 0)
						hdrlines = self.decodeFullText(hdrBytes)
						msgHdrs.append('\n'.join(hdrlines))
			finally:
				server.quit()
			assert len(msgSizes) == len(msgHdrs)
			self.trace('load headers exit')
			return msgHdrs, msgSizes, False

	def downloadAllMessages(self, process=None, loadfrom=1):
		self.trace('loading messages...')
		fetchlimit = FETCHLIMIT
		server = self.connect()
		try:
			(msgCounts, allBytes) = server.stat()
			msgTexts = []
			msgSizes = []
			if i in range(loadfrom, msgCounts+1):
				if process:
					process(i, msgCounts)
				if fetchlimit and (i<= msgCounts-fetchlimit):
					mailtext = 'Subject: -- skipped mail--\n\n skipped mail\n'
					msgTexts.append(mailtext)
					msgSizes.append(len(mailtext))
				else:
					(resp, msgBytes, respsz) = server.retr(i)
					msglines = self.decodeFullText(msgBytes)
					msgTexts.append('\n'.join(msglines))
					msgSizes.append(respsz)
		finally:
			server.quit()
		assert len(msgTexts) == msgCounts - loadfrom + 1
		return msgTexts, msgSizes, True

	def deleteMessages(self, msgNumList, progess=None):
		self.trace('deleting mails...')
		server = self.connect()
		try:
			for (ix, msgNum) in enumerate(msgNumList):
				if process:
					process(ix+1, len(msgNumList))
				server.dele(msgNum)
		finally:
			server.quit()

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

