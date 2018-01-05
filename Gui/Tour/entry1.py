from tkinter import *
from quitter import Quitter

def fetch(ent):
	print('Input => %s' % ent.get())

root = Tk()
ent = Entry(root)
ent2 = Entry(root)

ent.insert(0, 'Type words here')
ent.pack()
ent.focus()
ent.bind('<Return>', (lambda evnt,ent=ent:fetch(ent)))
ent2.pack()

btn = Button(text='Fetch', command=(lambda ent=ent2:fetch(ent)))
btn.pack(side=LEFT)

Quitter(root).pack(side=RIGHT)
root.mainloop()

