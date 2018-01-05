import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage

imgDir = '../gif/'
if len(sys.argv) > 1:
	imgDir = sys.argv[1]
imgFiles = os.listdir(imgDir)

root = Tk()
root.title('Viewer')
quit = Button(root, text='Quit all', command=root.quit, font=('courier',35))
quit.pack()
savePhotos = []

for imgFile in imgFiles:
	imgpath = os.path.join(imgDir, imgFile)
	win = Toplevel()
	win.title(imgFile)
	try:
		imgObj = PhotoImage(file=imgpath)
		Label(win, image=imgObj).pack()
		print(imgpath, imgObj.width(), imgObj.height())
		savePhotos.append(imgObj)
	except:
		errmsg = 'skipping %s\n%s' % (imgFile, sys.exc_info()[1])
		Label(win, text=errmsg).pack()

root.mainloop()
