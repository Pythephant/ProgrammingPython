from tkinter import *
from quitter import Quitter

fields = 'Name', 'Job', 'Pay'

def fetch(entries):
	for ent in entries:
		print('%s input => %s' % (ent, ent.get()))

def makeForm(root, fields):
	entries = []
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=5, text=field)
		ent = Entry(row)
		ent.bind('<Return>',lambda event,ent=ent:fetch([ent]))
		row.pack(fill=X)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries.append(ent)
	return entries

if __name__ == '__main__':
	root = Tk()
	ents = makeForm(root, fields)
	passwd = Frame(root)
	passwd.pack(fill=X)
	Label(passwd, text='passwd').pack(side=LEFT)
	pEnt = Entry(passwd, show='*')
	pEnt.pack(side=RIGHT,expand=YES, fill=X)
	ents.append(pEnt)
	Button(root, text='FetchAll', command=(lambda ents=ents:fetch(ents))).pack(side=LEFT)
	Quitter(root).pack(side=RIGHT)
	root.mainloop()
