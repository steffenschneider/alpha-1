#!/usr/bin/env python3
# coding: utf-8

# Stil: Best of the Best Practices (https://gist.github.com/sloria/7001839)

import random
import tkinter

"""
Version 1:
- guess the solution of an addition of two simple numbers

TODO:
- generate random numbers       DONE
- calculation                   DONE
- click-event + compare results
- feature: wenn Kind drei Farben richtig hat darf es background-color wählen

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
__version__ = "0.5"
__maintainer__ = "Steffen Schneider"
__email__ = "nanosecond@web.de"
__status__ = "Development"


class MathProgram(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.geometry("400x400+300+150")  # field size
        self.run_game()

    def run_game(self):
        # create problem
        int_1, int_2, solution, wrong_solution, solution_position = self.create_problem()

        # text with the math question
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="center", fg="black", bg="yellow", text="Helvetica",
                              font=("Helvetica", 45))
        label.grid(column=0, row=0, columnspan=2, sticky='EW')
        self.labelVariable.set(str(int_1) + " + " + str(int_2))
        self.grid_columnconfigure(0, weight=1)  # stretch to the whole window size
        self.update()

        # answer fields (Buttons)
        answer_fields = [solution, wrong_solution]
        button2 = tkinter.Button(self, text=answer_fields[solution_position], font="Helvetica 65 bold",
                                 command=lambda: self.check_solution(2, solution_position), height=1, width=3,
                                 fg="black", bg="yellow")
        button2.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

        button3 = tkinter.Button(self, text=answer_fields[1 ^ solution_position], font="Helvetica 65 bold",
                                 command=lambda: self.check_solution(3, solution_position), height=1, width=3,
                                 fg="black", bg="yellow")
        button3.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    def create_problem(self):
        # create question
        int_1 = random.randint(0, 6)
        int_2 = random.randint(0, 6)
        solution = int_1 + int_2
        wrong_solution = solution + random.choice([-3, -2, -1, 1, 2, 3])  # don't use 0 here
        solution_position = random.randint(0, 1)  # change the position of the solution randomly
        return int_1, int_2, solution, wrong_solution, solution_position

    def check_solution(self, button_number, solution_position):
        if button_number - 2 == solution_position:
            print("PASS")
        else:
            print("FAIL")
        self.run_game()


if __name__ == "__main__":
    app = MathProgram(None)
    app.title('Math is fun - Addition')
    app.mainloop()
