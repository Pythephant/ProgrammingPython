gifdir = '../gif/'
from tkinter import *
from PIL import ImageTk
win = Tk()
img = ImageTk.PhotoImage(file=gifdir+'2.jpeg')
Button(win, image=img, command=(lambda:print('lalaall'))).pack()
win.mainloop()
