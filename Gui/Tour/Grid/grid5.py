from tkinter import *

rowNum, colNum = 4,5

rows = []
for i in range(rowNum):
	cols = []
	for j in range(colNum):
		ent = Entry(relief='ridge')
		ent.grid(row=i, column=j, sticky=NSEW)
		ent.insert('end', '%d.%d'%(i,j))
		cols.append(ent)
	rows.append(cols)

def onPress():
	for row in rows:
		for col in row:
			print(col.get(), end=' ')
		print()

Button(text='Fetch', command=onPress).grid()
mainloop()
