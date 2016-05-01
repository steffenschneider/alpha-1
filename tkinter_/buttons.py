import tkinter

Tkinter = tkinter
from tkinter import Tk, Frame, BOTTOM, LEFT, Button

root = Tk()
frame = Frame(root, height=500, width=500)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

root.mainloop()
