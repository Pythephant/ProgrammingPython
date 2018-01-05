from tkinter import *
content = 'Oh by the way, which one\'s Pink?'
defaultConfig = {'bg':'pink','font':('times',16,'italic')}

msg = Message(text=content)
msg.config(**defaultConfig)
msg.pack(fill=X, expand=YES)

label = Label(text=content)
label.config(**defaultConfig)
label.pack(fill=X, expand=YES)

mainloop()
