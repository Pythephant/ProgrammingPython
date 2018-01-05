from tkinter import *
from gui6 import Hello

class HelloExtender(Hello):
	def makeWidgets(self):
		Hello.makeWidgets(self)
		Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

	def message(self):
		print('Hello %s' %self.data)


if __name__ == '__main__':
	HelloExtender().mainloop()
