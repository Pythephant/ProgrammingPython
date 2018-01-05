from tkinter import *
widget = Button(text='Spam', padx = 10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='pencil')
widget.config(bd=8, relief=RAISED)
widget.config(state=DISABLED)
widget.config(bg='green',fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()
