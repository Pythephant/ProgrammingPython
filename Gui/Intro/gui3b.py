import sys
from tkinter import *

root = Tk()
widget = Button(text='Press to exit',command=(lambda:print('time to exit') or sys.exit()))
widget.pack()
mainloop()
