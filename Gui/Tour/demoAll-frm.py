from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRation', 'demoScale']

def addComponents(root):
	parts = []
	for demo in demoModules:
		module = __import__(demo)
		part = module.Demo(root)
		part.config(bd=2, relief=GROOVE)
		part.pack(side=LEFT, expand=YES, fill=BOTH)
		parts.append(part)
	return parts

def dumpState(parts):
	for part in parts:
		print(part.__module__ + ':',end=' ')
		if hasattr(part, 'report'):
			part.report()
		else:
			print('None')

if __name__ == '__main__':
	root = Tk()
	root.title('Frames')
	Label(root, text='Multiple Frame Demo', bg='white').pack()
	Button(root, text='All States', command=(lambda:dumpState(parts))).pack(fill=X)
	Quitter(root).pack(fill=X)
	parts = addComponents(root)
	root.mainloop()
