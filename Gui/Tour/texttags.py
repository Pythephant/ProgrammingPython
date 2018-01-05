from tkinter import *
from PIL import ImageTk

def hello(event):
	print('Got tag event')

root = Tk()
text = Text(root)
text.config(font=('courier',15,'normal'))
text.config(width=20, height=12)
text.pack(expand=YES, fill=BOTH)
text.insert('end', 'this is\n\nthe meaning\n\nof life.\n\n')

btn = Button(text, text='Spam', command=(lambda: hello(0)))
btn.pack()
text.window_create('end', window=btn)
text.insert('end', '\n')
img = ImageTk.PhotoImage(file='../gif/1.jpg')
text.image_create(END, image=img)

text.tag_add('demo', '1.5' ,'1.7')
text.tag_add('demo', '3.0','3.3')
text.tag_add('demo', '5.3', '5.7')
text.tag_config('demo', background='purple')
text.tag_config('demo', foreground='white')
text.tag_config('demo', font=('times', 18, 'underline'))
text.tag_add('demo2', '1.0', '1.4')
text.tag_config('demo2', font=('times', 10, 'bold'))
text.tag_bind('demo','<Double-1>', hello)
text.tag_bind('demo2', '<Button-1>', lambda event:print('lala'))
root.mainloop()


