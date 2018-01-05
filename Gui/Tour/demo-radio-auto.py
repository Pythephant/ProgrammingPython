from tkinter import *
root = Tk()
var = IntVar()
for i in range(10):
	rad = Radiobutton(root, text=str(i), variable=var, value=i)
	rad.pack(side=LEFT)
root.mainloop()
print(var.get())
