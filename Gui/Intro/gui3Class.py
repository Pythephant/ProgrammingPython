import sys, time
from tkinter import *

class HelloGui:
	def __init__(self, seconds):
		self.seconds = seconds
		Button(None, text='press and %s to exit'%seconds,command = self.quit).pack()

	def quit(self):
		for i in range(self.seconds):
			print('Warning: %s seconds to exit' % (self.seconds - i))
			time.sleep(1)
		print('Exiting')
		sys.exit()

HelloGui(3)
mainloop()
