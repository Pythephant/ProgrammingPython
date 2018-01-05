from tkinter import *

class Alarm(Frame):
	def __init__(self, msecs=1000):
		self.msecs = msecs
		Frame.__init__(self)
		self.pack()
		stopper = Button(self, text='Stop the beeps!',command=self.quit)
		stopper.pack()
		stopper.config(bg='navy', fg='white',bd=8)
		self.stopper = stopper
		self.repeater()

	def repeater(self):
		print('be be be')
		self.stopper.flash()
		self.after(self.msecs, self.repeater)
		print('after the after method')

if __name__ == '__main__':
	Alarm(msecs=2000).mainloop()
