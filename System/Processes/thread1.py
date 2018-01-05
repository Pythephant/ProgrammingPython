import _thread,time

def child(tid):
	time.sleep(1)
	print('Hello from thread',tid)

def parent():
	i = 0
	while True:
		i += 1
		_thread.start_new_thread(child, (i,))
		if input('Main thread to continue(q to quit),now the i is %s:\n'%i) == 'q':
			break


if __name__ == '__main__':
	parent()
