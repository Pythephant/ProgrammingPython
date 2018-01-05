from tkinter import *

class ScrolledList(Frame):
	def __init__(self, options, parent=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.makeWidgets(options)

	def makeWidgets(self, options):
		sbar = Scrollbar(self)
		listbox = Listbox(self, relief=SUNKEN)
		listbox.config(selectmode=EXTENDED)
		listbox.config(yscrollcommand=sbar.set)
		sbar.config(command=listbox.yview)
		sbar.pack(side=RIGHT, fill=Y)
		listbox.pack(side=LEFT, fill=BOTH, expand=YES)

		for label in options:
			listbox.insert('end', label)
		listbox.bind('<Double-1>', self.handleList)
		self.listbox = listbox

	def handleList(self, event):
		index = self.listbox.curselection()
		selection = self.listbox.get(index)
		self.runCommand(selection)

	def runCommand(self, selection):
		print('You selected:' , selection)

if __name__ == '__main__':
	options = (('Lumberjack-%s' %x ) for x in range(20))
	ScrolledList(options).mainloop()
		
