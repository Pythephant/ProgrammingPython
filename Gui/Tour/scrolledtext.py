from tkinter import *

class ScrolledText(Frame):
	def __init__(self, parent=None, text='', fileName=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.makeWidgets()
		self.setText(text, fileName)

	def makeWidgets(self):
		sbar = Scrollbar(self)
		text = Text(self, relief=SUNKEN)
		sbar.config(command=text.yview)
		text.config(yscrollcommand=sbar.set)
		sbar.pack(side=RIGHT, fill=Y)
		text.pack(side=LEFT, expand=YES, fill=BOTH)
		self.text = text

	def setText(self, data='', fileName=None):
		if fileName:
			data = open(fileName, 'r').read()
		self.text.delete('1.0', 'end')
		self.text.insert('1.0', data)
		self.text.mark_set(INSERT, '1.0')
		self.text.focus()

	def getText(self):
		return self.text.get('1.0', 'end-1c')
		#return self.text.get('1.0', 'end')

if __name__ == '__main__':
	root = Tk()
	if len(sys.argv) >1 :
		st = ScrolledText(fileName=sys.argv[1])
	else:
		st = ScrolledText(text='Worlds\n go here')
	def show(event):
		print(st.getText())
	root.bind('<Key-Escape>', show)
	root.mainloop()

