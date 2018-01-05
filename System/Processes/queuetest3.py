import threading, queue, time

numconsumer = 2
numproducer = 4
nummessages = 4

dataQueue = queue.Queue()

def producer(idnum):
	for msgnum in range(nummessages):
		time.sleep(idnum)
		msg = '[prducer id=%d, count=%d]'%(idnum,msgnum)
		print(msg)
		dataQueue.put(msg)

def consumer(idnum):
	while True:
		time.sleep(0.1)
		try:
			data = dataQueue.get(block=False)
			print('consumer',idnum,'got=>',data)
		except queue.Empty:
			pass

if __name__ == '__main__':
	waitFor = []
	for i in range(numconsumer):
		thread = threading.Thread(target = consumer, args = (i,))
		thread.daemon = True
		thread.start()
	for i in range(numproducer):
		thread = threading.Thread(target = producer, args = (i,))
		waitFor.append(thread)
		thread.start()

	for thread in waitFor:
		thread.join()
	print('Main thread exit.')
