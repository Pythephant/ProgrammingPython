import os, time

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = ('Spam %03d at %s' % (zzz, time.time())).encode()
		os.write(pipeout, msg)
		zzz = (zzz + 1) % 5

def parent():
	pipein, pipeout = os.pipe()
	if os.fork() == 0:
		child(pipeout)
	else:
		while True:
			line = os.read(pipein, 32).decode()
			print('Parent %d got [%s] at %s' %(os.getpid(), line, time.time()))


if __name__ == '__main__':
	parent()
