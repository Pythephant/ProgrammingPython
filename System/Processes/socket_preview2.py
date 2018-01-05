from socket import socket, AF_INET, SOCK_STREAM
import time
import threading
import os

port = 55555
host = 'localhost'

def srvHandle(conn, addr):
	print('+++++++++++++++++++++++++++++')
	print('server accept conn,addr:[%s,%s] at %s' %(conn, addr, time.time()))
	data = conn.recv(1024)
	reply = 'server got:[%s]' % data.decode()
	print(reply)
	conn.send(reply.encode())
	print('+++++++++++++++++++++++++++++')

def server():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(('',port))
	sock.listen(5)
	while True:
		conn, addr = sock.accept()
		threading.Thread(target=srvHandle, args=(conn,addr)).start()


def client():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host, port))
	msg = 'p[%s] t[%s] send at %s' % (os.getpid(), threading.get_ident(), time.time())
	sock.send(msg.encode())
	reply = sock.recv(1024)
	sock.close()
	print('client got: [%s]' % reply.decode())

if __name__ == '__main__':
	sthread = threading.Thread(target = server)
	sthread.daemon = True
	sthread.start()
	for i in range(5):
		threading.Thread(target = client).start()
