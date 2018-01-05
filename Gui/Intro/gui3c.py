import sys
from tkinter import *
import time

def timeToExit(seconds):
	for i in range(seconds):
		print('Warning, %ss to exit' % str(seconds - i))
		time.sleep(1)
	sys.exit()

if __name__ == '__main__':
	seconds = int(sys.argv[1])
	root = Tk()
	widget = Button(text='Press and %s seconds to exit'%seconds, command = (lambda:timeToExit(seconds)))
	widget.pack()
	root.mainloop()
