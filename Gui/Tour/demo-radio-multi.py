from tkinter import *
root = Tk()
var1 = StringVar()
for i in range(3):
	rad = Radiobutton(root, text=str(i), variable=var1, value=str(i))
	rad.pack(side=LEFT)

var1.set('1')
var2 = StringVar()
for i in range(5):
	rad=Radiobutton(root, text=str(i*10), variable=var2, value=str(i*10))
	rad.pack(side=RIGHT)
var2.set(' ')
root.mainloop()
