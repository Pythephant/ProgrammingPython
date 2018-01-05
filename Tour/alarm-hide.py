from tkinter import *
import alarm

class Alarm(alarm.Alarm):
	def __init__(self, msecs=1000):
		self.shown = False
		alarm.Alarm.__init__(self, msecs)

	def repeater(self):
		print('be be be :',self.shown)
		if self.shown:
			self.stopper.pack_forget()
		else:
			self.stopper.pack()
		self.shown = not self.shown
		self.after(self.msecs, self.repeater)

if __name__ == '__main__':
	Alarm(2000).mainloop()
