import os,time
from multiprocessing import Process

def action(arg):
	print(os.getpid(),arg)
	time.sleep(55555)

if __name__ == '__main__':
	p = Process(target=action, args = ('ttt',))
	p.start()
