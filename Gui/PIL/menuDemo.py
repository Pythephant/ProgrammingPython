from tkinter import *
from tkinter.messagebox import *
import os
from PIL import ImageTk

class NewMenuDemo(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.crtWidget()
		self.master.title('Toolbars and Menus')
		self.master.iconname('tkpython')

	def crtWidget(self):
		self.makeMenuBar()
		self.makeToolBar()
		l = Label(self, text='Menu and Toolbar Demo')
		l.config(relief=SUNKEN, width=40, height=10, bg='white')
		l.pack(expand=YES, fill=BOTH)

	def makeMenuBar(self):
		self.menuBar = Menu(self.master)
		self.master.config(menu=self.menuBar)
		self.addFileMenu()
		self.addEditMenu()
		self.addImgMenu()

	def makeToolBar(self):
		toolBar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
		toolBar.pack(side=BOTTOM, fill=X)
		Button(toolBar, text='Quit', command=self.quit).pack(side=RIGHT)
		Button(toolBar, text='Hello', command=self.greeting).pack(side=LEFT)

	def addFileMenu(self):
		menu = Menu(self.menuBar)
		menu.add_command(label='Open...',command=self.notdone)
		menu.add_command(label='Quit',command=self.quit)
		self.menuBar.add_cascade(label='File',underline=0,menu=menu)

	def addEditMenu(self):
		menu = Menu(self.menuBar)
		menu.add_command(label='Paste',command=self.notdone)
		menu.add_command(label='SPam', command=self.greeting)
		menu.add_separator()
		menu.add_command(label='Delete', command=self.greeting)
		menu.entryconfig(4, state=DISABLED)
		self.menuBar.add_cascade(label='Edit', underline=0, menu = menu)

	def addImgMenu(self):
		dirPath = '../gif/thumbs/'
		photoFiles = os.listdir(dirPath)
		pullDown = Menu(self.menuBar)
		self.photoObjs = []
		for photoFile in photoFiles:
			filePath = os.path.join(dirPath, photoFile)
			img = ImageTk.PhotoImage(file=filePath)
			pullDown.add_command(image=img,command=self.notdone)
			self.photoObjs.append(img)
		self.menuBar.add_cascade(label='Image',underline=0, menu=pullDown)

	def greeting(self):
		showinfo('greeting', 'Greetings')

	def notdone(self):
		showerror('Not implemented', 'Not Available')

	def quit(self):
		if askyesno('verify quit', 'Are you sure to quit?'):
			Frame.quit(self)


if __name__ == '__main__':
	NewMenuDemo().mainloop()
