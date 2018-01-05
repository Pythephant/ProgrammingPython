import time
import queue
import os
from multiprocessing import Process, Queue

class Counter(Process):
	label = '  $'
	def __init__(self, start, queue):
		self.state = start
		self.queue = queue
		Process.__init__(self)

	def run(self):
		for i in range(3):
			time.sleep(1)
			self.state += 1
			print(self.label, self.pid, self.state)
			self.queue.put([self.pid, self.state])
		print(self.label, self.pid, '- finished')

if __name__ == '__main__':
	print('start',os.getpid())
	expected = 9

	post = Queue()
	p = Counter(100, post)
	q = Counter(1000, post)
	r = Counter(10000, post)

	p.start()
	q.start()
	r.start()

	while expected:
		time.sleep(0.5)
		try:
			data = post.get(block = False)
		except queue.Empty:
			print('no data yet ...')
		else:
			print('posted:', data)
			expected -= 1
	p.join()
	q.join()
	r.join()
	print('finished', os.getpid(), 'p:%s, q:%s, r:%s' % (p.exitcode, q.exitcode, r.exitcode))
