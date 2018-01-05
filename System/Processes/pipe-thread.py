import os, time, threading

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = ('%s spam %03d at %s\n' % (threading.get_ident(), zzz, time.time())).encode()
		os.write(pipeout, msg)
		zzz = (zzz + 1)%5

def parent(pipein):
	pipein = os.fdopen(pipein)
	while True:
		line = pipein.readline().strip()
		print('Parent %d got [%s] at %s' % (threading.get_ident(), line, time.time()))

if __name__ == '__main__':
	pipein, pipeout = os.pipe()
	threading.Thread(target = child, args = (pipeout,)).start()
	threading.Thread(target = child, args = (pipeout,)).start()
	parent(pipein)
