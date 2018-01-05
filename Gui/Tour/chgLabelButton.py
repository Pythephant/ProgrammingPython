from dialogTable import demos
from tkinter import *

def chgColor(label):
	tps, color = demos['Color']()
	if color:
		label.config(bg=color)
		print('Color changed')

if __name__ == '__main__':
	root = Tk()
	label = Label(root, text='Lala')
	label.pack(fill=BOTH)
	label.config(bg='#f0f0f0')
	button = Button(root, text='Click to change color', command = lambda handler = chgColor,label=label: handler(label)).pack(fill=BOTH)
	root.mainloop()
