import tkinter

Tkinter = tkinter
from tkinter import Tk, Frame, BOTTOM, Button, Label, StringVar, Radiobutton

from datetime import datetime

fontsize = 16


class App:
    def __init__(self, master):

        frame = Frame(master, height=200, width=200)
        # frame.pack_propagate(0) # don't shrink
        frame.pack()

        ##################################
        # MODE                           #
        ##################################

        a = Label(master, text="MODE", font=("Helvetica", fontsize), fg='white')
        a.pack()
        MODE = [
            ("STATIC", "static"),
            ("CYCLE", "cycle"),
        ]

        v = StringVar()
        # v.set("static") # initialize

        for text, mode in MODE:
            b = Radiobutton(master, text=text, font=("Helvetica", fontsize),
                            variable=v, value=mode, indicatoron=0)
            b.pack()

        ##################################
        # AVERAGES                       #
        ##################################

        c = Label(master, text="AVERAGES", font=("Helvetica", fontsize), fg='white')
        c.pack()

        MODES = [
            ("     1     ", 1),
            ("     2     ", 2),
            ("     4     ", 4),
        ]

        v = StringVar()
        # v.set("static") # initialize

        for text, mode in MODES:
            d = Radiobutton(master, text=text, font=("Helvetica", fontsize),
                            variable=v, value=mode, indicatoron=0)
            # a['fg'] = 'white'
            d.pack()

        # SCANNUMMER

        # SCANGROESSE

        ##################################
        # DATE + TIME                    #
        ##################################


        e = Label(master, text="DATE: " + str(datetime.now().strftime("%d")) + "." \
                               + str(datetime.now().strftime("%m")) + "." \
                               + str(datetime.now().strftime("%Y")) \
                  , font=("Helvetica", fontsize))
        e.pack()
        f = Label(master, text="TIME: " + str(datetime.now().strftime("%H")) + ":" \
                               + str(datetime.now().strftime("%M")) + ":" \
                               + str(datetime.now().strftime("%S")) \
                  , font=("Helvetica", fontsize))
        f.pack()

        ##################################
        # BUTTON: START MEASUREMENT      #
        ##################################

        self.hi_there = Button(frame, text="START MEASUREMENT" \
                               , font=("Helvetica", fontsize), command=self.say_hi)
        self.hi_there.pack(side=BOTTOM)

    ##################################
    # DEFINITIONS                    #
    ##################################

    def say_hi(self):
        print('aa')


root = Tk()

app = App(root)

root.mainloop()
