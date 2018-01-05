import os, sys, find

def cleanpyc(rootDir, toRemoved = True):
	removed = 0
	found = 0
	for filename in find.find('*.pyc', rootDir):
		found += 1
		if toRemoved:
			os.remove(filename)
			removed += 1
	return found, removed


if __name__ == '__main__':
	rootDir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]
	found, removed = cleanpyc(rootDir)
	print('Found',found,'files, removed',removed)
