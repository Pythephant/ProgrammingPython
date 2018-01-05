from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(variables):
	for variable in variables:
		print('Input => %s' % variable.get())

def makeForm(root, fields):
	form = Frame(root)
	left = Frame(form)
	rite = Frame(form)
	form.pack(fill=X)
	left.pack(side=LEFT)
	rite.pack(side=RIGHT, expand=YES, fill=X)

	variables = []
	for field in fields:
		lab = Label(left, width=5, text=field)
		ent = Entry(rite)
		lab.pack()
		ent.pack(fill=X)
		var = StringVar()
		ent.config(textvariable=var)
		var.set('enter here')
		variables.append(var)

	return variables

if __name__ =='__main__':
	root = Tk()
	variables = makeForm(root, fields)
	Button(root, text='Fetch', command=(lambda : fetch(variables))).pack(side=LEFT)
	Quitter(root).pack(side=RIGHT)
	root.bind('<Return>', (lambda event: fetch(variables)))
	root.mainloop()
