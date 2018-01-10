from socket import *
import sys,os,time
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
		conn.send(b'Echo => %s at %s' % (data, now()))
	conn.close()
	os._exit(0)

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
		reapClient(actClients)
		pid = os.fork()
		if pid == 0:
			handleClient(conn)
		else:
			actClients.append(pid)


if __name__ == '__main__':
	dispatcher()
		
