from tkinter import *
colors = ['red','white','blue']

def gridbox(parent):
	Label(parent, text='Grid:').grid(columnspan=2)
	row = 1
	for color in colors:
		lab = Label(parent, text=color, width=25)
		ent = Entry(parent, bg=color, width=50)
		lab.grid(row=row,column=0, sticky=NSEW)
		ent.grid(row=row, column=1, sticky=NSEW)
		ent.insert(0, 'grid')
		parent.rowconfigure(row, weight=row)
		row += 1
	parent.columnconfigure(1, weight=1)

def packbox(parent):
	Label(parent, text='Pack:').pack()
	for color in colors:
		row = Frame(parent)
		lab = Label(row, text=color, width=25)
		ent = Entry(row, bg=color, width=50)
		row.pack(side=TOP, expand=YES, fill=BOTH)
		lab.pack(side=LEFT, expand=YES, fill=BOTH)
		ent.pack(side=RIGHT, expand=YES, fill=BOTH)

root = Tk()
gridbox(Toplevel())
packbox(Toplevel())
Button(root, text='Quit', command=root.quit).pack()
root.mainloop()


