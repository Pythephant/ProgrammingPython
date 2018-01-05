import os
import sys

def lister(root):
	for (dirname, subdirs, files) in os.walk(root):
		print('[' + dirname + ']')
		for fname in files:
			path = os.path.join(dirname , fname)
			print(path)

if __name__ == '__main__':
	lister(sys.argv[1])
