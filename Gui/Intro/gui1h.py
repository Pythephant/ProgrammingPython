from tkinter import *
import time

root = Tk()
widget = Label(root,text= 'Hello GUI world!')
widget.pack()
root.mainloop()
time.sleep(5)
widget['text'] = 'Bye Bye'
widget.pack()

