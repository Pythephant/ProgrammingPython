import os, sys
readsize = 1024

def join(fromdir, tofile):
	outputfile = open(tofile, 'wb')
	parts = os.listdir(fromdir)
	parts.sort()
	for filename in parts:
		filepath = os.path.join(fromdir, filename)
		inputfile = open(filepath, 'rb')
		while True:
			filebytes = inputfile.read(readsize)
			if not filebytes:
				break
			outputfile.write(filebytes)
		inputfile.close()
	outputfile.close()

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == '-help':
		print('Usage: join.py [from-dir-name to-file-name]')
	else:
		if len(sys.argv) !=3 :
			interactive = True
			fromdir = input('Directory contain the part files?	')
			tofile = input('Name of file to be recreated?	')
		else:
			interactive = False
			fromdir, tofile = sys.argv[1:3]
		absfrom, absto = map(os.path.abspath, [fromdir, tofile])
		print('Joining ',[absfrom],'to make',[absto])

		try:
			join(fromdir, tofile)
		except:
			print('Error occur joining files:')
			print(sys.exc_info()[0], sys.exc_info()[1])
		else:
			print('Join complete: see', absto)

