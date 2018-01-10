import socketserver, time

def now():
	return time.ctime(time.time())

class MyClientHandler(socketserver.BaseRequestHandler):
	def handle(self):
		print('New connection:', self.client_address,'at',now())
		time.sleep(3)
		while True:
			data = self.request.recv(1024)
			if not data:
				break
			reply = 'Echo => %s at %s' % (data, now())
			self.request.send(reply.encode())
		self.request.close()

if __name__ == '__main__':
	myHost, myPort = '', 50007
	myAddr = (myHost, myPort)
	server = socketserver.ThreadingTCPServer(myAddr, MyClientHandler)
	server.serve_forever()
