import poplib, smtplib, email.utils, sys
import re
from email.parser import Parser, BytesParser
from email.message import Message
import email
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
def formatToMessage(bytesList):
	msg = [email.message_from_bytes(mByte) for mByte in bytesList] 
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

def loadMessages(serverName, user, passwd, newerNum=10):
	
	server = fetchConnect(serverName, user, passwd)
	try:
		msgCount, msgTotalBytes = server.stat()
		newerNum = msgCount if newerNum < 0 else newerNum
		print('There are', msgCount,'messages, total bytes:',msgTotalBytes)
		print('Retrieving...')
		msgList = []
		for i in range(msgCount - newerNum + 1, msgCount+1):
			hdr, msgByteLines, octets = server.retr(i)
			msgList.append(b'\n'.join(msgByteLines))
	except:
		print('Error happened in loading messages')
		print(sys.exc_info[0],sys.exc_info[1])
	finally:
		server.quit()
	assert len(msgList) == newerNum
	msgList = formatToMessage(msgList)
	return msgList

def deleteMessages(serverName, user, passwd, toDelete, verify=True):
	pass

def showIndex(msgList, i):
	totalNum = len(msgList)
	i = totalNum if i < 0 else i
	for n in range(totalNum - i,totalNum):
		print('[%d]'%n+'-'*50)
		for hdr in ('From','To','Date','Subject'):
			try:
				print('\t%-8s=>%s'%(hdr, msgList[n][hdr]))
			except KeyError:
				print('\t%-8s=>(unknown)'%hdr)

		

def showMessage(msgList, i):
	totalNum = len(msgList)
	i = totalNum if i<0 else i
	pattern = re.compile(r'charset="(.+)"')
	for n in range(totalNum - i, totalNum):
		print('[%d]'%n + '-'*50)
		for hdr in ('From','To','Date','Subject'):
			try:
				print('\t%-8s=>%s'%(hdr, msgList[n][hdr]))
			except KeyError:
				print('\t%-8s=>(unknown)'%hdr)
			for w in msgList[n].walk():
				if w.get_content_type() == 'text/plain':
					charSet = re.search(pattern, w['Content-Type']).group(1)
					print(w.get_payload(decode=True).decode(charSet))

def saveMessage(i, mailFile, msgList):
	pass

def msgNum(command):
	try:
		return int(command.split()[1])
	except:
		return -1

def interact(msgList, saveDir, serverName, user, passwd):
	showIndex(msgList, 10)
	toDelete = []
	print(helpText)
	while True:
		try:
			command = input('[Pymail] Action? (i, l, d, s, m, q, ?) ')
		except EOFError:
			command = 'q'
		#quit
		if command[0] == 'q':
			break
		#index
		elif command[0] == 'i':
			showIndex(msgList, msgNum(command))
		#show list
		elif command[0] == 'l':
			showMessage(msgList, msgNum(command))
		#save
		elif command[0] == 's':
			pass

		#delete:
		elif command[0] == 'd':
			pass

		#mail
		elif command[0] == 'm':
			sendMessage(serverName, user, passwd)

		#helpText
		elif command[0] == '?':
			print(helpText)
		else:
			print('What? --type "?" for commands help')
	return toDelete
	
if __name__ == '__main__':
	import getpass
	saveDir = 'savemail/'
	retrServer = 'pop.yeah.net'
	sendServer = 'smtp.yeah.net'
	user = 'jason_wujiakun@yeah.net'
	print('Password to login[%s]'%user)
	passwd = getpass.getpass()
	msgList = loadMessages(retrServer, user, passwd)
	toDelete = interact(msgList,saveDir,sendServer,user,passwd)
	if toDelete:
		deleteMessages(retrServer, user, passwd, toDelete)
	print('Bye')
