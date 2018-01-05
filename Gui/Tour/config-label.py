from tkinter import *

root = Tk()
labelFont = ('times', 20, 'bold italic')
widget = Label(root, text='Hello config world')
widget.config(font=labelFont)
widget.config(bg='black', fg='orange')
widget.config(height=3, width=20)
widget.config(cursor='pencil')
widget.pack(expand=YES, fill=Y)
root.mainloop()
