from tkinter import *
rownum, colnum = 4,5

for i in range(rownum):
	for j in range(colnum):
		lab = Label(text='%d.%d'%(i,j), relief='ridge')
		lab.grid(row=i, column=j, sticky=NSEW)

mainloop()
