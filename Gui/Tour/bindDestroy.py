from tkinter import *
import sys

root = Tk()
widget = Label(root, text='To be Destory')
widget.pack()
Button(root, text="exit", command=sys.exit).pack()
widget.bind('<Destroy>', lambda event:print(event))
root.mainloop()
