import threading, time
import random

count = 0

def adder():
	global count
	if count < 100:
		time.sleep(random.random())
		count += 1

threads = []
for i in range(150):
	thread = threading.Thread(target = adder, args = ())
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

print(count)
