#!/usr/bin/env python3
# coding: utf-8

# Stil: Best of the Best Practices (https://gist.github.com/sloria/7001839)

import tkinter

"""
Können wir erstmal ein Spiel machen wo man die Lösung auf einem von zwei
Buttons angezeigt bekommt?

TODO:
- generate random numbers
- calculation
- click-event
- compare results

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

CHANGELOG:
- 30.04.16 Button size changed
"""

__author__ = "Steffen Schneider, Erik Streb"
__copyright__ = "..."
__credits__ = ["Steffen Schneider, Erik Streb"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Steffen Schneider"
__email__ = "nanosecond@web.de"
__status__ = "Development"


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
                              font=("Helvetica", 45))
        label.grid(column=0, row=0, columnspan=2, sticky='EW')
        self.labelVariable.set("1 + 2")
        self.grid_columnconfigure(0, weight=1)  # stretch to the whole window size
        self.update()

        # answer fields
        button2 = tkinter.Button(self, text="3", font="Helvetica 65 bold",
                                 command=self.OnButtonClick, height=1, width=3)
        button2.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

        button3 = tkinter.Button(self, text="4", font="Helvetica 65 bold",
                                 command=self.OnButtonClick, height=1, width=3)
        button3.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

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
