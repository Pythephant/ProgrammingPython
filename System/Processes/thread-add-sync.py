import threading, time
import random

count = 0

def adder(lock,i):
	global count
	lock.acquire()
	print('[%s] the count is:'%i,count)
	if count < 100:
		time.sleep(random.random())
		count += 1
	lock.release()

lock = threading.Lock()
threads = []
for i in range(150):
	thread = threading.Thread(target = adder, args = (lock,i))
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

print(count)
