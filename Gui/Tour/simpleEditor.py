from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename
from quitter import Quitter
from scrolledtext import ScrolledText
import sys,os

class SimpleEditor(ScrolledText):
	def __init__(self, parent=None, fileName=None):
		frm = Frame(parent)
		frm.pack(fill=X)
		self.fileName = fileName
		Button(frm, text='Save', command=self.onSave).pack(side=LEFT)
		Button(frm, text='SaveAs',command=self.onSaveAs).pack(side=LEFT)
		Button(frm, text='Cut', command=self.onCut).pack(side=LEFT)
		Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
		Button(frm, text='Find', command=self.onFind).pack(side=LEFT)
		Quitter(frm).pack(side=RIGHT)
		ScrolledText.__init__(self, parent, fileName = fileName)
		self.text.config(font=('courier',15,'normal'))

	def onSaveAs(self):
		filePath = asksaveasfilename()
		if filePath:
			allText = self.getText()
			open(filePath, 'w').write(allText)
	
	def onSave(self):
		if self.fileName:
			allText = self.getText()
			open(self.fileName, 'w').write(allText)
		else:
			self.onSaveAs()

	def onCut(self):
		textCopy = self.text.get('sel.first','sel.last')
		self.text.delete(SEL_FIRST, SEL_LAST)
		self.clipboard_clear()
		self.clipboard_append(textCopy)

	def onPaste(self):
		try:
			textToPaste = self.selection_get(selection='CLIPBOARD')
			self.text.insert(INSERT, textToPaste)
		except:
			print('Error happen on Paste\n',sys.exc_info()[1])
	
	def onFind(self):
		target = askstring('SimpleEditor', 'Search String?')
		if target:
			startIndex = self.text.search(target, INSERT, END)
			if startIndex:
				print(startIndex)
				pastit = startIndex + ('+%dc' % len(target))
				self.text.mark_set(INSERT, pastit)
				self.text.see(INSERT)
				self.text.focus()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		SimpleEditor(fileName=sys.argv[1]).mainloop()
	else:
		SimpleEditor().mainloop()
		
