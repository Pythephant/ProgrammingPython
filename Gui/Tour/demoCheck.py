from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		self.tools()
		Label(self, text='Check demos').pack()
		self.variables = []
		for key in demos:
			var = IntVar()
			cb = Checkbutton(self, text=key, variable = var)
			cb.pack(side=LEFT)
			self.variables.append((key,var))

	def report(self):
		for var in self.variables:
			print(var[0],'=>',var[1].get())

	def tools(self):
		frm = Frame(self)
		frm.pack(side=RIGHT)
		Button(frm, text='state', command=self.report).pack(fill=X)
		Quitter(frm).pack(fill=X)

if __name__ == '__main__':
	Demo().mainloop()
