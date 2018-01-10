from socket import *
import sys,os,time
from multiprocessing import Process
serverHost = ''
serverPort = 50007

def now():
	return time.ctime(time.time())

def handleClient(conn):
	time.sleep(5)
	while True:
		data = conn.recv(1024)
		if not data:
			break
		reply = 'Echo => %s at %s' % (data, now()) 
		conn.send(reply.encode())
	conn.close()

def reapClient(actClients):
	while actClients:
		pid, stat = os.wait(0, os.WNOHANG)
		if not pid:
			break
		actClients.remove(pid)

def dispatcher():
	sockObj = socket(AF_INET, SOCK_STREAM)
	sockObj.bind((serverHost, serverPort))
	sockObj.listen(5)
	actClients = []
	while True:
		conn, addr = sockObj.accept()
		print('Server received a connection from %s at %s' % (addr, now()))
		#reapClient(actClients)
		Process(target=handleClient, args=(conn,)).start()


if __name__ == '__main__':
	dispatcher()
		
