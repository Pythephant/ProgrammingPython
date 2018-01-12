import time, os, sys
import _thread as thread
from socket import *

blksize = 1024
defaultHost = 'localhost'
defaultPort = 60001

helpText = '''
Usage...
server=> getfile.py -mode server 		[-host hhh] [-port nnn]
client=> getfile.py [-mode client] -file fff [-host hhh] [-port nnn]
'''

def now():
	return time.asctime()

def parseCmd():
	argDict = {}
	args = sys.argv[1:]
	while len(args) >= 2:
		argDict[args[0]] = args[1]
		args = args[2:]
	return argDict

def client(host, port, filePath):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host, port))
	sock.send((filePath + '\n').encode())
	fileName = os.path.split(filePath)[1]
	fileObj = open(fileName, 'wb')
	while True:
		data = sock.recv(blksize)
		if not data:
			break
		fileObj.write(data)
	sock.close()
	fileObj.close()
	print('Client got',filePath,'at',now())
	
def server(host, port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(5)
	while True:
		clientSock, clientAdrr = sock.accept()
		print('Server connected by',clientAdrr,'at',now())
		thread.start_new_thread(transThread,(clientSock,))

def transThread(clientConn):
	sockStream = clientConn.makefile('r')
	filePath = sockStream.readline().rstrip()
	try:
		fileObj = open(filePath,'rb')
		while True:
			byteStream = fileObj.read(blksize)
			if not byteStream:
				break
			sent = clientConn.send(byteStream)
			assert sent == len(byteStream)
	except:
		print('Error Downloading:',filePath,'at',now())
	fileObj.close()
	clientConn.close()


def main(args):
	host = args.get('-host',defaultHost)
	port = args.get('-port',defaultPort)
	if args.get('-mode') == 'server':
		server(host, port)
	elif args.get('-file'):
		client(host, port, args['-file'])
	else:
		print(helpText)

	

if __name__ == '__main__':
	args = parseCmd()
	main(args)
