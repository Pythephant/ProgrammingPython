from tkinter import *
from launchmodes import PortableLauncher

demoModules = ['demoDlg', 'demoRation', 'demoCheck', 'demoScale']

for demo in demoModules:
	PortableLauncher(demo, demo+'.py')()

root = Tk()
root.title('Process')
Label(root,text='Multiple program demo: command lines',bg='yellow').pack()
root.mainloop()
