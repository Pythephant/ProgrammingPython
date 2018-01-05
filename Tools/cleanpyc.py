import os, sys


def cleanpyc(rootDir, toRemoved = True):
	found = 0
	removed = 0
	for (thisDir, subDirs, fileNames) in os.walk(rootDir):
		for fileName in fileNames:
			if fileName.endswith('.pyc'):
				fullname = os.path.join(thisDir, fileName)
				if toRemoved:
					try:
						os.remove(fullname)
						removed += 1
					except:
						errType, inst = sys.exc_info()[:2]
						print('*'*5,'Failed', filename, errType, inst)
				found += 1
	return found, removed

if __name__ == '__main__':
	rootDir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]	
	found, removed = cleanpyc(rootDir)
	print('Found',found,'files, removed',removed)
