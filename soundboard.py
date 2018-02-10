import os

from tkinter import *

app =TK()
app.title('Sound Board')

Fcanvas =Canvas( bg="black", height=600, width=800)

def sound1():
	os.system("")

var Intvar()

rb1 Radiobutton(app, text "Play audio one", variable =var, vaule 1, command sound1)
rb1.pack(anchor = W)

Fcanvas.pack()
app.mainloop()
