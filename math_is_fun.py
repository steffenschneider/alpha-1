#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# uuups deine Beschreibung ist weg. (Sorry)

import tkinter

"""
TODO:
HEAD
- anstatt grid canvas. nutzen; damit lässt sich die Position pixelgenau einstellen
"""

class math_program(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.geometry("400x400+300+150")  # field size

        # text with the math question
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="black")
        label.grid(column=0, row=0, columnspan=2, sticky='EW')
        self.labelVariable.set(u"1 + 2")

        self.grid_columnconfigure(0, weight=1)
        self.update()
        self.geometry(self.geometry())

        # answer fields
        button2 = tkinter.Button(self, text=u"3", command=self.OnButtonClick)
        button2.grid(column=0, row=1)
        button3 = tkinter.Button(self, text=u"4", command=self.OnButtonClick)
        button3.grid(column=1, row=1)

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get() + " (You clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + " (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    app = math_program(None)
    app.title('Math is fun')

    app.mainloop()
