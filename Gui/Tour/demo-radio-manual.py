from tkinter import *

buttons = []

def onPress(i):
	for btn in buttons:
		btn.deselect()
	buttons[i].select()

root = Tk()
for i in range(10):
	rad = Radiobutton(root, text=str(i), value=str(i),command=(lambda i=i:onPress(i)))
	rad.pack(side=LEFT)
	buttons.append(rad)

onPress(1)
root.mainloop()

