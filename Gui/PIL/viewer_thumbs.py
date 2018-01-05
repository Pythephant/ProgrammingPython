import os, sys, math
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

def makeThumbs(imgdir, size=(100,100), subdir='thumbs'):
	'''
	get thumbsneil image for all the images in a directory;for each image,
	create and save a new thumb , or load and return an existing thumb;
	make thumb dir if needed; returns a list of (image filename, thumb image object);
	'''
	thumbdir = os.path.join(imgdir, subdir)
	if not os.path.exists(thumbdir):
		os.mkdir(thumbdir)

	thumbs = []
	for imgfile in os.listdir(imgdir):
		thumbpath = os.path.join(thumbdir, imgfile)
		if os.path.exists(thumbpath):
			thumbobj = Image.open(thumbpath)
			thumbs.append((imgfile, thumbobj))
		else:
			print('making',thumbpath)
			imgpath = os.path.join(imgdir, imgfile)
			try:
				imgobj = Image.open(imgpath)
				imgobj.thumbnail(size, Image.ANTIALIAS)
				imgobj.save(thumbpath)
				thumbs.append((imgfile, imgobj))
			except:
				print('Skipping:',imgpath, sys.exc_info()[1])
	return thumbs

class ViewOne(Toplevel):
	'''
	to open the real image in the popup windows
	'''
	def __init__(self, imgdir, imgfile):
		Toplevel.__init__(self)
		self.title(imgfile)
		imgpath = os.path.join(imgdir, imgfile)
		imgobj = PhotoImage(file=imgpath)
		Label(self, image=imgobj).pack()
		print(imgpath, imgobj.width(), imgobj.height())
		self.savephoto = imgobj

def viewer(imgdir, kind=Toplevel, cols=None):
	win = kind()
	win.title('Viewer:' + imgdir)
	quit = Button(win, text='Quit', command=win.quit, bg='beige')
	quit.pack(fill=X, side=BOTTOM)
	thumbs = makeThumbs(imgdir)
	if cols is None:
		cols = int(math.ceil(math.sqrt(len(thumbs))))
	savephotos = []
	while thumbs:
		thumbrow, thumbs = thumbs[:cols], thumbs[cols:]
		row = Frame(win)
		row.pack(fill=BOTH)
		for (imgfile, imgobj) in thumbrow:
			photo = PhotoImage(imgobj)
			link = Button(row, text=imgfile,image=photo)
			handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
			link.config(command=handler)
			link.pack(side=LEFT, expand=YES)
			savephotos.append(photo)
	return win, savephotos

if __name__ == '__main__':
	imgdir = sys.argv[1] if len(sys.argv) >1 else '../gif/'
	root, savephotos = viewer(imgdir, kind=Tk)
	root.mainloop()
