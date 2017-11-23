"""
split and interactively page a string or file of text
"""

def more(text, numlines = 15):
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:
			print(line)
		if lines and input('More?(y/Y):') not in ('y','Y'):
			print('Bye bye!')
			break

if __name__ == '__main__':
	import sys
	more(open(sys.argv[1]).read(),10)
