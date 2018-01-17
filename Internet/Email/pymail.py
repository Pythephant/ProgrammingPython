import poplib, smtplib, email.utils
from email.parser import Parser, BytesParser
from email.message import Message
fetchEncoding = 'utf8'

helpText='''
Available commands:
i n		- index display n newest message, default 10
l n		- list the newest n messages, default 10
d n		- mark the number [n] message for deletion, 'A' for all
s n		- save the number [n] message for savving, 'A' for all
m		- compose and sent a new mail message
q		- quit pymail
?		- display this help text
'''
def formatToMessage(messageBytes):
	content = b'/n'.join(messageBytes)
	msg = BytesParser().parsebytes(content)
	return msg

def splitAddrs(field):
	pairs = email.utils.getaddresses([field])	#return[(name, addres)..]
	return [email.utils.formataddr(pair) for pair in pairs]

def inputMessage():
	pass

def sendMessage():
	pass

def connect(serverName, user, passwd):
	print('Connecting to "%s"'%serverName)
	server = poplib.POP3(serverName)
	server.user(user)
	server.pass_(passwd)
	print(server.getwelcome())
	return server

def loadMessages(serverName, user, passwd, loadStartIdx=1):
	server = connect(serverName, user, passwd)
	try:
		msgCount, msgTotalBytes = server.stat()
		print('There are', msgCount,'messages, total bytes:',msgTotalBytes)
		print('Retrieving...')
		msgList = []
		for i in range(loadStartIdx, msgCount+1):
			hdr, msgByteLines, octets = server.retr(i)
			msg = formatToMessage(msgByteLines)
			msgList.append(msg)
	except:
		print('Error happened in loading messages')
		print(sys.exc_info[0],sys.exc_info[1])
	finally:
		server.quit()
	assert len(msgList) == (msgCount - loadStartIdx + 1)
	return msgList

def deleteMessages(serverName, user, passwd, toDelete, verify=True):
	pass

def showIndex(msgList, i):
	pass

def showMessage(msgList, i):
	pass

def saveMessage(i, mailFile, msgList):
	pass

def msgNum(command):
	try:
		return int(command.split()[1])
	except:
		return -1

