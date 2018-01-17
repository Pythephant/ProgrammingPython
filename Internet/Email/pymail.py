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
	import sys
	From = input('From? ').strip()
	To = input('To? ').strip()
	To = splitAddrs(To)
	Subj = input('Title of the Email:').strip()
	print('Type message text, end with line="."')
	text = ''
	while True:
		line = sys.stdin.readline()
		if line == '.\n':
			break
		text += line
	return From, To, Subj, text

def sendMessage(serverName, user, passwd):
	From, To, Subj, text = inputMessage()
	msg = Message()
	msg['From'] = From
	msg['To'] = ', '.join(To)
	msg['Subject'] = Subj
	msg['Date'] = email.utils.formatdate()
	msg.set_payload(text)
	server = sendConnect(serverName, user, passwd)
	try:
		sendFailed = server.send_message(msg)
	except:
		print('Error - send failed')
	else:
		if sendFailed:
			print('Failed:',sendFailed)

def sendConnect(serverName, user, passwd):
	print('Connecting server:',serverName)
	server = smtplib.SMTP(serverName)
	server.login(user, passwd)
	return server

def fetchConnect(serverName, user, passwd):
	print('Connecting to "%s"'%serverName)
	server = poplib.POP3(serverName)
	server.user(user)
	server.pass_(passwd)
	print(server.getwelcome())
	return server

def loadMessages(serverName, user, passwd, loadStartIdx=1):
	server = fecthConnect(serverName, user, passwd)
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
	totalNum = len(msgList)
	for n in range(totalNum - i,totalNum):
		print('[%d]'%n+'-'*50)
		for hdr in ('From','To','Date','Subject'):
			try:
				print('\t%-8s=>%s'%(hdr, msgList[n][hdr]))
			except KeyError:
				print('\t-8s=>(unknown)'%hdr)

		

def showMessage(msgList, i):
	

def saveMessage(i, mailFile, msgList):
	pass

def msgNum(command):
	try:
		return int(command.split()[1])
	except:
		return -1

