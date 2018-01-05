from tkinter import *
from menu_win import makemenu

root = Tk()
for i in range(3):
	win = Toplevel(root)
	makemenu(win)
	Label(win, bg='black', height=5, width=25).pack()
Button(root, text='QuitAll', command=root.quit).pack()
root.mainloop()
