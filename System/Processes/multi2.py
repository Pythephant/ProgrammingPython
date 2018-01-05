import os
from multiprocessing import Process, Value, Array

count = 0
def showdata(label, val, arr):
	msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
	print(msg % (label, os.getpid(), count, val.value, list(arr)))

def updater(value, arr):
	global count
	count += 1
	value.value += 1
	for i in range(len(arr)):
		arr[i] += 1

if __name__ == '__main__':
	scalar = Value('i', 0)
	vector = Array('d', 10)
	showdata('parent start', scalar, vector)

	#spawn child passing in shared memory
	p = Process(target = showdata, args=('child', scalar, vector))
	p.start()
	p.join()

	print('\nloop1 (updates in parent, serial child)...')
	for i in range(len(vector)):
		count += 1
		scalar.value += 1
		vector[i] += 1
		p = Process(target= showdata, args=( 'process %s' % i, scalar, vector))
		p.start()
		p.join()

	#update in parent show in child parallel
	print('\nloop2 (updates in parent, parallel child)...')
	ps = []
	for i in range(len(vector)):
		count += 1
		scalar.value += 1
		vector[i] += 1
		p = Process(target = showdata, args = ('process %s' %i , scalar, vector))
		p.start()
		ps.append(p)
	for p in ps:
		p.join()

	print('\nloop3 (updates in serial child)...')
	for i in range(len(vector)):
		p = Process(target = updater, args = (scalar, vector))
		p.start()
		p.join()
	showdata('temp parent', scalar, vector)

	#update in parallel
	print('\nloop4 (updates in parallel child)...')
	ps = []
	for i in range(len(vector)):
		p = Process(target = updater, args = (scalar, vector))
		p.start()
		ps.append(p)
	for p in ps:
		p.join()
	showdata('final data result', scalar, vector)

