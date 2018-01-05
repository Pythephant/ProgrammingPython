import os, time

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = ('%s Spam %03d at %s\n' % (os.getpid(), zzz, time.time())).encode()
		os.write(pipeout, msg)
		zzz = (zzz + 1) % 5

def parent():
	pipein, pipeout = os.pipe()
	if os.fork() == 0:
		os.close(pipein)
		child(pipeout)
	elif os.fork() == 0:
		os.close(pipein)
		child(pipeout)	
	else:
		os.close(pipeout)
		pipein = os.fdopen(pipein)
		while True:
			line = pipein.readline().strip()
			print('Parent %d got [%s] at %s' %(os.getpid(), line, time.time()))


if __name__ == '__main__':
	parent()
