import os, sys
trace = False

dirname = '.' if len(sys.argv)==1 else sys.argv[1]

allsizes = []
for (thisDir, subDirs, fileNames) in os.walk(dirname):
	if trace:
		print(thisDir)
	for filename in fileNames:
		if filename.endswith('.py'):
			if trace:
				print('...', filename)
			fullname = os.path.join(thisDir,filename)
			filesize = os.path.getsize(fullname)
			allsizes.append((filesize, fullname))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
