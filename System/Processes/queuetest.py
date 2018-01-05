import _thread as thread, queue, time

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
	for i in range(numconsumer):
		thread.start_new_thread(consumer,(i,))
	for i in range(numproducer):
		thread.start_new_thread(producer, (i,))

	time.sleep((numproducer-1)*nummessages + 1)
	print('Main thread exit.')
