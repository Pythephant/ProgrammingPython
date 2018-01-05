import sys, os
maxsizeload = 1000*1024
blksize = 500*1024

def copyFile(pathFrom, pathTo, maxsizeload = maxsizeload):
	if os.path.getsize(pathFrom) <= maxsizeload:
		bytesFrom = open(pathFrom, 'rb').read()
		open(pathTo, 'wb').write(bytesFrom)
	else:
		fileFrom = open(pathFrom, 'rb')
		fileTo = open(pathTo, 'wb')
		while True:
			bytesFrom = fileFrom.read(blksize)
			if not bytesFrom:
				break
			fileTo.write(bytesFrom)

def copyTree(dirFrom, dirTo, trace = 0):
	fcount = 0
	dcount = 0
	for filename in os.listdir(dirFrom):
		pathFrom = os.path.join(dirFrom, filename)
		pathTo = os.path.join(dirTo, filename)
		if os.path.isdir(pathFrom):
			if trace:
				print('copying dir', pathFrom, 'to', pathTo)
			try:
				if not os.path.exists(pathTo):
					os.mkdir(pathTo)
				below = copyTree(pathFrom, pathTo, trace)
				fcount += below[0]
				dcount += below[1]
				dcount += 1
			except:
				print('Error creating', pathTo, '--skipped')
				print(sys.exc_info()[0], sys.exc_info()[1])
		else:
			try:
				if trace > 1:
					print('copying',pathFrom,'to',pathTo)
				copyFile(pathFrom, pathTo)
				fcount += 1
			except:
				print('Error copying', pathFrom, 'to', pathTo,'--skipped')
				print(sys.exc_info()[0], sys.exc_info()[1])
	return (fcount, dcount)


def getArgs():
	try:
		dirFrom, dirTo = sys.argv[1:3]
	except:
		print('Usage error: cpall.py dirFrom dirTo')
	else:
		if not os.path.isdir(dirFrom):
			print('Error: dirFrom is not a directory')
		elif not os.path.exists(dirTo):
			os.mkdir(dirTo)
			print('Note: dirTo',dirTo,'was created')
			return (dirFrom, dirTo)
		else:
			print('Warning: dirTo',dirTo,'already exists')
			toCover = input('Do you want to cover it?(y/Y)>>>')
			if toCover!='y' and toCover!='Y':
				return
			if hasattr(os.path, 'samefile'):
				same = os.path.samefile(dirFrom, dirTo)
			else:
				same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
			if same:
				print('Warning: dirFrom same as dirTo. Nothing to be done.')
			else:
				return (dirFrom, dirTo)

if __name__ == '__main__':
	import time
	dirstuple = getArgs()
	trace = 0 if len(sys.argv)<4 else int(sys.argv[3])
	argtuple = dirstuple + (trace,)
	if dirstuple:
		print('Copying...')
		start = time.clock()
		fcount, dcount = copyTree(*argtuple)
		print('Copied', fcount,'files,', dcount,'directories', end='')
		print('in', time.clock() - start, 'seconds')


