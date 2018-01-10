from socket import *
import _thread as thread
import time

myHost = 'localhost'
myPort = 5555

def now():
	return time.ctime(time.time())

def clientHandler(conn, addr, otherConns):
	while True:
		data = conn.recv(1024)
		reply = '[%s at %s]:%s' % (addr, now(), data.decode())
		print(reply)
		for key in otherConns:
			otherConns[key].send(reply.encode())

if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind( (myHost, myPort))
	sock.listen(5)
	connections = {} 
	while True:
		conn, addr = sock.accept()
		print('New Connection:',addr,'at',now())
		thread.start_new_thread(clientHandler, (conn, addr, connections))
		connections[addr] = conn


