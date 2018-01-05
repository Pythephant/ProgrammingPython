from tkinter import *
rowNum, colNum = 5,4

root = Tk()
rows = []
for i in range(rowNum):
	cols = []
	for j in range(colNum):
		ent = Entry(root, relief='ridge')
		ent.grid(row=i, column=j, sticky=NSEW)
		ent.insert('end', '%d.%d'%(i,j))
		cols.append(ent)
	rows.append(cols)

sums = []
for j in range(colNum):
	lab = Label(root, text='?')
	lab.grid(row=rowNum, column=j, sticky=NSEW)
	sums.append(lab)

def onPrint():
	for row in rows:
		for col in row:
			print(col.get(), end=' ')
		print()
	print()

def onSum():
	totals = [0]*colNum
	for i in range(rowNum):
		for j in range(colNum):
			totals[j] += eval(rows[i][j].get())
	for j in range(colNum):
		sums[j].config(text=str(totals[j]))

def onClear():
	for row in rows:
		for col in row:
			col.delete(0, 'end')
			col.insert('end','0.0')
	for col in sums:
		col.config(text='0.0')

Button(root, text='Sum', command=onSum).grid(row=rowNum+1,column=0)
Button(root, text='Print', command=onPrint).grid(row=rowNum+1, column=1)
Button(root, text='Clear',command=onClear).grid(row=rowNum+1, column=2)
Button(root, text='Quit', command=root.quit).grid(row=rowNum+1,column=3)
root.mainloop()
