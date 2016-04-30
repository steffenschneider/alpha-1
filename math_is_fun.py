#!/usr/bin/env python3
# coding: utf-8
# !!! wir machen bitte alles mit utf-8, wir sind im Jahr 2016!!!
# Stil: Best of the Best Practices (https://gist.github.com/sloria/7001839)

import tkinter

"""
Können wir erstmal ein Spiel machen wo man die Lösung auf einem von zwei
Buttons angezeigt bekommt?

TODO:
HEAD
- eventuell anstatt grid canvas nutzen; damit lässt sich die Position
  pixelgenau einstellen

PLAN:
- at the beginning
-- the difficulty is set
- the math question is shown dependent on the difficulty
- the user chooses a solution from one of the buttons
- if clicked
-- PASS or FAIL is shown
-- the score is update
-- after 5 secs a new question is shown
- the game finishes after 10-15 questions
"""

class MathProgram(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.geometry("400x400+300+150")  # field size

        # text with the math question
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,
            anchor="center", fg="white", bg="black", text="Helvetica",
            font=("Helvetica", 25))
        label.grid(column=0, row=0, columnspan=2, sticky='EW')
        self.labelVariable.set("1 + 2")
        self.grid_columnconfigure(0, weight=1)  # stretch to the whole window size
        self.update()
        #self.geometry(self.geometry()) # <-- wozu ist das hier? das ist doch
                                        # schon oben definiert

        # answer fields
        # TODO: Button-Größe und ausrichten
        button2 = tkinter.Button(self, text="3", command=self.OnButtonClick)
        button2.grid(column=0, row=1)

        button3 = tkinter.Button(self, text="4", command=self.OnButtonClick)
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
    app = MathProgram(None)
    app.title('Math is fun')
    app.mainloop()
