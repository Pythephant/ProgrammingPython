from tkinter import *
root = Tk()
scl = Scale(root, label='Simple Scale', from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=YES, fill=Y)

def report(scl):
	print(scl.get())

Button(root, text='state', command=(lambda scl=scl:report(scl))).pack(side=RIGHT)
root.mainloop()
