from glob import glob
from tkinter import *
from demoRation import Demo
from PIL import ImageTk
import random

imgDir = '../gif/'

class ButtonPicsDemo(Frame):
	def __init__(self, imgDir=imgDir, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		self.lbl = Label(self, text='none', bg='blue', fg='red')
		self.pic = Button(self, text='Press Me', command=self.draw, bg='black')
		self.lbl.pack(fill=BOTH)
		self.pic.pack(pady=10)
		Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
		files = glob(imgDir+'*')
		self.images = [(x, ImageTk.PhotoImage(file=x)) for x in files]
		print(files)

	def draw(self):
		name, photo = random.choice(self.images)
		self.lbl.config(text=name)
		self.pic.config(image=photo)

if __name__ == '__main__':
	ButtonPicsDemo().mainloop()
