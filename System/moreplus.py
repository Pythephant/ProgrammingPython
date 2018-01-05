"""
split and interactively page a string or file of text
split and interactively page a string, file, or stream of text to stdout; when run as a script, page stdin or file whose name is passed on cmdline; if input is stdin, can't use it for user reply--use platform-specific tools or GUI;
"""
import sys

def getreply():
	'''
	read a reply key from interactive user
	even if stdin redirected to a file or pipe
	'''

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
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read(),10)
