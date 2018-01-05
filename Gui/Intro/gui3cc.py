import sys
from tkinter import *

def quit(msg):
	print('bye bye',msg)
	sys.exit()


msg = ['hello 1']
widget = Button(text='press',command=lambda msg=msg:quit(msg))
msg.append('hello 2')
widget.pack()
widget.mainloop()

