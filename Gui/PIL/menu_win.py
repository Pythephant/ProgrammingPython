from tkinter import *
from tkinter.messagebox import showerror

def notdone():
	showerror('Not implemented', 'Not yet available')

def makemenu(win):
	top = Menu(win)
	win.config(menu=top)

	fileMenu = Menu(top)
	fileMenu.add_command(label='New...', command=notdone, underline=0)
	fileMenu.add_command(label='Open...', command=notdone, underline=1)
	fileMenu.add_command(label='Quit', command=win.quit, underline=0)
	top.add_cascade(label='File', menu=fileMenu)

	edit = Menu(top, tearoff=False)
	edit.add_command(label='Cut', command=(lambda:print('Cut Cut...')), underline=0)
	edit.add_command(label='Paste', command=notdone, underline=2)
	edit.add_separator()
	top.add_cascade(label='Edit', menu=edit, underline=0)

	subEdit = Menu(edit, tearoff=True)
	subEdit.add_command(label='Spam', command=lambda:print('Spam '*3),underline=0)
	subEdit.add_command(label='Egg', command=notdone, underline=0)
	subEdit.add_command(label='ToQuit',command=win.quit, underline=0)
	edit.add_cascade(label='Stuff', menu=subEdit)

if __name__ == '__main__':
	root = Tk()
	root.title('Menu_Win')
	makemenu(root)
	msg = Label(root, text='Window menu basics')
	msg.pack(expand=YES, fill=BOTH)
	msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
	root.mainloop()
	
