from tkinter import SUNKEN, Tk, Canvas, Frame


class Ball:
    def __init__(self, canvas, xy, ink, vecx, vecy):
        self.canvas = canvas
        self.id = self.canvas.create_oval(5, 5, 15, 15, fill=ink)
        self.canvas.move(self.id, xy[0], xy[1])
        if vecx > 0:
            self.vecx = vecx
            self.start = self.right
        else:
            self.vecx = -vecx
            self.start = self.left
        self.vecy = vecy

    def __call__(self):
        return self.start  # get things going

    def right(self):
        xy = self.canvas.coords(self.id)
        if xy[2] >= self.canvas.winfo_width():
            return self.left()
        self.canvas.move(self.id, self.vecx, self.vecy)
        return self.right

    def left(self):
        xy = self.canvas.coords(self.id)
        if xy[0] <= 0:
            return self.right()
        self.canvas.move(self.id, -self.vecx, self.vecy)
        return self.left


root = Tk()
root.title("Blobs")
root.resizable(0, 0)
frame = Frame(root, bd=15, relief=SUNKEN)
frame.pack()
canvas = Canvas(frame, width=500, height=300, bd=0, highlightthickness=0)
canvas.pack()
speed = 0.02
dy = 20
items = [
    Ball(canvas, (0, 10), "red", 0.201, 0.020),
    Ball(canvas, (0, 21), "yellow", 0.20, 0.025),
    Ball(canvas, (0, 32), "green", 0.2013, 0.03)
]

root.update()  # fix geometry

# loop over items
try:
    while 1:
        for i in range(len(items)):
            items[i] = items[i]()
            root.update_idletasks()  # redraw
        root.update()  # process events
except:
    pass  # to avoid errors when the window is closed
