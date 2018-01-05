import _thread as thread

numOfThread = 10
mutexLock = thread.allocate_lock()
exitmutex = [False]*10

def counter(tid, count):
	for i in range(count):
		mutexLock.acquire()
		print('tid[%s] => %s' %(tid,i))
		mutexLock.release()
	exitmutex[tid] = True


for i in range(numOfThread):
	thread.start_new_thread(counter, (i,100))

while False in exitmutex:
	pass
print('Main thread exit.')
