import _thread as thread
from socket import *
myHost = 'localhost'
myPort = 5555

def listen(sock):
	while True:
		data = sock.recv(1024)
		print(data.decode())

if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((myHost, myPort))
	thread.start_new_thread(listen, (sock,))
	while True:
		msg = input()
		sock.send(msg.encode())

