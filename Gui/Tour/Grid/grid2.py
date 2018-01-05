from tkinter import *
colors = ['red','green','orange','white','yellow','blue']

def gridbox(parent):
	r = 0
	for c in colors:
		Label(parent, text=c, relief=RIDGE, width=25).grid(row=r, column=0)
		Entry(parent, bg=c, relief=SUNKEN, width=50).grid(row=r, column=1)
		r += 1

def packbox(parent):
	for c in colors:
		row = Frame(parent)
		lab = Label(row, text=c, relief='ridge', width=25)
		ent = Entry(row, bg=c, relief='sunken', width=50)
		row.pack(side=TOP)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT)
		ent.insert(0, 'pack')

if __name__ == '__main__':
	root = Tk()
	gridbox(Toplevel())
	packbox(Toplevel())
	Button(root, text='Quit', command=root.quit).pack()
	root.mainloop()
