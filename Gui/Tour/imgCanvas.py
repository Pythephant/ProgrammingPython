from tkinter import *
from PIL import ImageTk

imgDir = '../gif/'
root = Tk()
img = ImageTk.PhotoImage(file=imgDir+'1.jpg')
canv = Canvas(root)
canv.pack(fill=BOTH)
canv.create_image(1,1,image=img,anchor=NW)
canv.config(cursor='pencil',bg='black')
root.mainloop()
