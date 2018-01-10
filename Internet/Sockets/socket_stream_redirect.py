import sys
from socket import *
port = 50008
host = 'localhost'

def initListenerServer(host=host, port=port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind( (host, port))
	sock.listen(5)
	conn, addr = sock.accept()
	return conn

def redirectOut(host=host, port=port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host, port))
	fout = sock.makefile('w')
	sys.stdout = fout
	return sock

def redirectIn(host=host, port=port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host, port))
	fin = sock.makefile('r')
	sys.stdin = fin
	return sock

def redirectClient(host=host, port=port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host,port))
	fout = sock.makefile('w')
	fin = sock.makefile('r')
	sys.stdout = fout
	sys.stdin = fin
	return sock

def redirectServer(host=host, port=port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((host,port))
	sock.listen(5)
	conn, addr = sock.accept()
	fout = sock.makefile('w')
	fin = sock.makefile('r')
	sys.stdout = fout
	sys.stdin = fin
	return conn
