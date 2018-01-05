import _thread as thread, os

exitstat = 0

def child():
	global exitstat
	exitstat += 1
	threadid = thread.get_ident()
	print('Hello from child', threadid, exitstat)
	#os._exit(exitstat)			#this will kill the process thus main thread
	thread.exit()
	print('Never reached')

def parent():
	while True:
		thread.start_new_thread(child, ())
		if input() == 'q':
			break

if __name__ == '__main__':
	parent()
