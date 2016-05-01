#!/usr/bin/env python3
# coding: utf-8

__author__ = "Steffen Schneider"
__copyright__ = "..."
__credits__ = ["Steffen Schneider"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Steffen Schneider"
__email__ = "nanosecond@web.de"
__status__ = "Development"

"""
Balls in a TKinter-GUI moving downwards because of gravity.
This is an interactive game

TODO
- create a circle
- move circle according to gravity laws
- add obstacle
"""

import time
import tkinter


class Gravity_game(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.geometry("400x400+300+150")  # field size
        self.configure(background='#090')  # green color
        # self.run_game()  # first call


        C = tkinter.Canvas(tkinter.Tk(), bg="blue", height=250, width=300)
        coord = 10, 50, 240, 210
        arc = C.create_arc(coord, start=0, extent=150, fill="red")

    def run_game(self):
        count = 0
        while 1:
            count += 1
            print(count)
            time.sleep(1)
            self.update()


if __name__ == "__main__":
    app = Gravity_game(None)
    app.title('Gravity game - Version ' + str(__version__))
    app.mainloop()
