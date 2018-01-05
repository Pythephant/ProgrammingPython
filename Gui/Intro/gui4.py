from tkinter import *

def greeting():
	print('Hello stdout world!')

win = Frame()
win.pack(expand=YES, fill=BOTH)
Button(win, text='Hello', command=greeting).pack(side=LEFT,anchor=SW)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT,anchor=SE)

win.mainloop()
