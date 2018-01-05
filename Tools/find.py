import fnmatch, os

def find(pattern, startdir=os.curdir):
	for (thisDir, subDirs, filenames) in os.walk(startdir):
		for name in subDirs + filenames:
			if fnmatch.fnmatch(name, pattern):
				fullPath = os.path.join(thisDir, name)
				yield fullPath

def findlist(pattern, startdir=os.curdir, isSorted = False):
	matches = list(find(pattern, startdir))
	if isSorted:
		matches.sort()
	return matches


if __name__ == '__main__':
	import sys
	print(sys.argv)
	namepattern = sys.argv[1]
	startdir = os.curdir if len(sys.argv)<3 else sys.argv[2]
	for name in find(namepattern, startdir):
		print(name)
