import os 
import time
from multiprocessing import Pool

def power(x):
	time.sleep(0.1)
	temp = 2**x
	print(os.getpid(),temp)
	return temp 

if __name__ == '__main__':
	worker = Pool(processes = 5)
	results = worker.map(power, [2]*10)
	print(results[:5])
	print(results[-2:])

	results = worker.map(power, range(100))
	print(results[:16])
	print(results[-2:])
