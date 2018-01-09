from socket import *
import time

host = 'localhost'
port = 50007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.bind( (host, port) )
sockObj.listen(5)

while True:
	conn, addr = sockObj.accept()
	print('Server accepts a connection from:',addr)
	while True:
		data = conn.recv(1024)
		time.sleep(3)
		if not data:
			break
		conn.send(b'Echo => ' + data)
	conn.close()
