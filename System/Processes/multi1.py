from multiprocessing import Process,Lock
import os

def whoami(label, lock):
	msg = '%s: name:%s, pid:%s'
	print(msg % (label, __name__, os.getpid()))

if __name__ == '__main__':
	whoami('function call', None)

	p = Process(target = whoami, args = ('spawned child', None))
	p.start()
	p.join()

	for i in range(5):
		Process(target = whoami, args = ('run process %s' % i, None)).start()


	print('Main process exit.')
