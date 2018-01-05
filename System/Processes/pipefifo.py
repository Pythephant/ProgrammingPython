import os, time, sys
fifoname = './tmp/pipefifo'

def child():
	pipeout = os.open(fifoname, os.O_WRONLY)
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = '%s spam %03d at %s\n' %(os.getpid(), zzz, time.time())
		os.write(pipeout, msg.encode())
		zzz = (zzz + 1) % 5

def parent():
	pipein = open(fifoname, 'r')
	while True:
		line = pipein.readline().strip()
		print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

if __name__ == '__main__':
	if not os.path.exists(fifoname):
		os.mkfifo(fifoname)
	if len(sys.argv) == 1:
		parent()
	else:
		child()
