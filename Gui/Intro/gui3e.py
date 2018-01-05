import sys
from tkinter import *

def hello(event):
	print(event)
	print('Press twice to exit')

def quit(event):
	print(event)
	print('Bye I must to go...')
	sys.exit()

widget = Button(text='Press once to get Info and twice to exit')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)

widget.mainloop()

