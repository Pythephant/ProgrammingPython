import _thread as thread
import time

def counter(tid, count):
	for i in range(count):
		#time.sleep(1)
		print('tid[%s] => %s' % (tid, i))

if __name__ == '__main__':
	for i in range(5):
		thread.start_new_thread(counter, (i, 100))

	time.sleep(6)
	print('Main thread exiting')
