#!/usr/bin/env python

import random

import tkinter

Tkinter = tkinter

# Screen resolution:
RESX = 800
RESY = 600


class ColoredBoxesWin:
    def __init__(self):

        self.mw = Tkinter.Tk()
        self.mw.option_add("*font", ("Arial", 12, "normal"))
        self.mw.title("Colored Boxes")
        self.mw.geometry("+90+45")

        self.cv = Tkinter.Canvas(self.mw,
                                 bg="white",
                                 width=RESX,
                                 height=RESY)

        self.cv.pack()

        speccicolors = ("black", "blue",
                        "grey", "white")

        for i in range(5, RESY - 30, 50):
            for u in range(25, RESX - 50, 50):
                c = random.randrange(len(speccicolors))

                self.cv.create_rectangle(u, i, u + 45, i + 45,
                                         outline=speccicolors[c],
                                         fill=speccicolors[c])

        self.btn = Tkinter.Button(self.mw,
                                  text="Ok",
                                  command=self.mw.destroy)

        self.btn.bind(sequence="<Return>", func=self.bindFunc)
        self.btn.focus()

        self.btn.pack(side=Tkinter.RIGHT,
                      padx=10,
                      pady=10)

        self.mw.mainloop()

    def bindFunc(self, a):
        self.mw.destroy()


if __name__ == "__main__":
    app = ColoredBoxesWin()
