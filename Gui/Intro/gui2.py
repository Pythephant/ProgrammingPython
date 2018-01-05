from tkinter import *
button = Button(None, text="press me to exit", command=sys.exit)
button.pack()
Label(text='Hello widget World').pack(side=TOP)
mainloop()
