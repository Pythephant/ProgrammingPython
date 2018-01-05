from tkinter import *
from tkinter.messagebox import showerror

def notdone():
	showerror('Not implemented','This Function Do not Available')

def makeMenu(win):
	menuBar = Frame(win)
	menuBar.pack(side=TOP, fill=X)

	fbutton = Menubutton(menuBar, text='File', underline=0)
	fbutton.pack(side=LEFT)
	fileMenu = Menu(fbutton)
	fileMenu.add_command(label='New...', command=notdone, underline=0)
	fileMenu.add_command(label='Open...',command=notdone,underline=0)
	fileMenu.add_command(label='Quit',command=win.quit,underline=0)
	fbutton.config(menu=fileMenu)

	ebutton = Menubutton(menuBar, text='Edit', underline=5)
	ebutton.pack(side=LEFT)
	editMenu = Menu(ebutton)
	editMenu.add_command(label='Copy', command=(lambda:print('Copy Copy')), underline=0)
	editMenu.add_command(label='Paste...',command=notdone,underline=0)
	editMenu.add_separator()
	ebutton.config(menu=editMenu)

	subEditMenu = Menu(editMenu, tearoff=True)
	subEditMenu.add_command(label='Spam',underline=0)
	subEditMenu.add_command(label='Eggs', command=notdone)
	editMenu.add_cascade(label='Stuff',menu=subEditMenu, underline=0)
	return menuBar

if __name__ == '__main__':
	root = Tk()
	root.title('Menu Frame')
	makeMenu(root)
	msg = Label(root, text='Frame menu basics')
	msg.config(relief=SUNKEN, width=40, height=25)
	msg.config(bg='beige')
	msg.pack(expand=YES, fill=BOTH)
	root.mainloop()

