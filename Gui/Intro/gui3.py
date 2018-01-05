import sys
from tkinter import *

def quit():
	print('Button pressed, bye bye!')
	sys.exit()

widget = Button(text='Hello world, press to exit',command = quit)
widget.pack()
widget.mainloop()
