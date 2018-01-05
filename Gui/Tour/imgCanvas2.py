from tkinter import *
from PIL import ImageTk
import sys

imgDir='../gif/'
filename = '1.jpg' if len(sys.argv)<2 else sys.argv[1]
root = Tk()
img = ImageTk.PhotoImage(file=imgDir+filename)
canv = Canvas(root)
canv.pack(expand=YES,fill=BOTH)
canv.config(cursor='watch', bg='blue')
canv.config(width=img.width(), height=img.height())
canv.create_image(2,2, image=img, anchor=NW)
root.mainloop()
