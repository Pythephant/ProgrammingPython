from tkinter import *

def showPosEvent(event):
	print('Widget=%s X=%s Y=%s'%(event.widget, event.x, event.y))

def showAllEvent(event):
	print(event)
	for attr in dir(event):
		if not attr.startswith('__'):
			print(attr, '=>', getattr(event, attr))

def onKeyPress(event):
	print('got key press:',event.char)

def onArrowKey(event):
	print('got up arrow key press:',event.char)

def onReturnKey(event):
	print('got return key press:', event.char)

def onLeftClick(event):
	print('got left mouse button click:',end=' ')
	showPosEvent(event)

def onRightClick(event):
	print('got left mouse button click:',end=' ')
	showPosEvent(event)

def onMiddleClick(event):
	print('got middle mouse button click:', end = ' ')
	showPosEvent(event)
	showAllEvent(event)

def onLeftDrag(event):
	print('got left mouse button drag:', end=' ')
	showPosEvent(event)

def onDoubleLeftClick(event):
	print('got double left mouse click:', end=' ')
	showPosEvent(event)
	event.widget.quit()

root = Tk()
labelfont = ('courier', 20, 'bold underline')
widget = Label(root, text='Hello bind world')
widget.config(bg='red', font=labelfont)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>', onLeftClick)
widget.bind('<Button-3>', onRightClick)
widget.bind('<Button-2>', onMiddleClick)
widget.bind('<Double-1>', onDoubleLeftClick)
widget.bind('B1-Motion>', onLeftDrag)

widget.bind('<KeyPress>', onKeyPress)
widget.bind('<Up>', onArrowKey)
widget.bind('<Return>', onReturnKey)
widget.bind('<Down>', onArrowKey)

root.title('Click me')
root.mainloop()
