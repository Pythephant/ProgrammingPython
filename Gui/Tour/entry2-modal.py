from tkinter import *
from entry2 import fields, makeForm, fetch

def show(entries, win):
	fetch(entries)
	win.destroy()

def ask():
	win = Toplevel()
	ents = makeForm(win, fields)
	Button(win, text='OK', command=(lambda: show(ents, win))).pack()
	win.grab_set()
	win.focus_set()
	win.wait_window()

root = Tk()
Button(root, text='Dialog', command=ask).pack()

root.mainloop()
