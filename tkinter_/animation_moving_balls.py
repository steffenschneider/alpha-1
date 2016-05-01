import tkinter

Tkinter = tkinter
from tkinter import Tk, Frame, Canvas


class Blob:
    def __init__(self, canvas, xy, ink, delta):

        self.canvas = canvas

        self.id = self.canvas.create_oval(
            -10 - abs(delta), -10,
            11 + abs(delta), 11,
            fill=ink
        )

        self.canvas.move(self.id, xy[0], xy[1])

        if delta > 0:
            self.delta = delta
            self.start = self.right
        else:
            self.delta = -delta
            self.start = self.left

    def __call__(self):
        return self.start  # get things going

    def right(self):

        xy = self.canvas.coords(self.id)
        if xy[2] >= self.canvas.winfo_width():
            return self.left()

        self.canvas.move(self.id, self.delta, 0)

        return self.right

    def left(self):

        xy = self.canvas.coords(self.id)
        if xy[0] <= 0:
            return self.right()

        self.canvas.move(self.id, -self.delta, 0)

        return self.left


root = Tk()
root.title("Blobs")
root.resizable(0, 0)

frame = Frame(root, bd=5)
frame.pack()

canvas = Canvas(frame, width=500, height=200, bd=0, highlightthickness=0)
canvas.pack()

speed = 0.2
dy = 5
items = [
    Blob(canvas, (100, 2 * dy), "red", 6 * speed),
    Blob(canvas, (100, 3 * dy), "blue", 7 * speed),
    Blob(canvas, (100, 4 * dy), "green", 8 * speed),
    Blob(canvas, (100, 5 * dy), "gold", 9 * speed),
    Blob(canvas, (100, 6 * dy), "red", 10 * speed),
    Blob(canvas, (100, 7 * dy), "blue", 11 * speed),
    Blob(canvas, (100, 8 * dy), "green", 12 * speed),
    Blob(canvas, (100, 9 * dy), "gold", 13 * speed),
    Blob(canvas, (100, 10 * dy), "red", 14 * speed),
    Blob(canvas, (100, 11 * dy), "blue", 15 * speed),
    Blob(canvas, (100, 12 * dy), "green", 16 * speed),
    Blob(canvas, (100, 13 * dy), "gold", 17 * speed),
    Blob(canvas, (100, 14 * dy), "red", 18 * speed),
    Blob(canvas, (100, 15 * dy), "blue", 19 * speed),
    Blob(canvas, (100, 16 * dy), "green", 20 * speed),
    Blob(canvas, (100, 17 * dy), "gold", 21 * speed),
]

root.update()  # fix geometry

# loop over items

try:
    while 1:
        for i in range(len(items)):
            items[i] = items[i]()
            root.update_idletasks()  # redraw
        root.update()  # process events
except TclError:
    pass  # to avoid errors when the window is closed
