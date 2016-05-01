import tkinter

Tkinter = tkinter
from tkinter import Tk, Frame, Label, TOP

from time import strftime
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import struct


class App:
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        self.press = Label(self.frame, text='Press escape key to quit!')
        self.press.pack(side=TOP)

        self.lab = Label(self.frame, text='  ')
        self.lab.pack()

        self.newtime()

        root.bind("<Escape>", self.Exit)
        root.geometry("1000x900")
        root.title('Messprogramm')

        self.counter = 0

        self.f = open('C:/Dokumente und Einstellungen/schnei17/Desktop/\
uwb_daten/avg2_2000/201106151327231_cycle_avg_2_modul_74.uwb', "rb")  # rb = read binary
        self.data1 = np.zeros((511, 100), dtype=np.int)
        self.data2 = np.zeros((511, 100), dtype=np.int)
        self.data3 = np.zeros((511, 100), dtype=np.int)
        self.data4 = np.zeros((511, 100), dtype=np.int)

        self.fig = Figure(figsize=(7, 5), dpi=130)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.show()
        self.canvas.get_tk_widget().place(x=1, y=170)

        self.fig1 = self.fig.add_subplot(141)
        self.fig2 = self.fig.add_subplot(142)
        self.fig3 = self.fig.add_subplot(143)
        self.fig4 = self.fig.add_subplot(144)

        self.Run = True

    def newtime(self):
        self.lab['text'] = strftime("%H:%M:%S")

    def newdataplot(self):

        self.f.seek(36 + 2080 * ((self.counter * 8) + 0))
        self.data = self.f.read(4 * 511)
        self.data = struct.unpack('511i', self.data)
        self.data = list(self.data)
        self.data = np.array(self.data)[np.newaxis]
        self.data = self.data.T
        self.data1 = np.concatenate((self.data1[:, :self.counter], self.data, self.data1[:, self.counter + 1:]), axis=1)
        self.fig1.imshow(self.data1)

        self.f.seek(36 + 2080 * ((self.counter * 8) + 1))
        self.data = self.f.read(4 * 511)
        self.data = struct.unpack('511i', self.data)
        self.data = list(self.data)
        self.data = np.array(self.data)[np.newaxis]
        self.data = self.data.T
        self.data2 = np.concatenate((self.data2[:, :self.counter], self.data, self.data1[:, self.counter + 1:]), axis=1)
        self.fig2.imshow(self.data2)

        self.f.seek(36 + 2080 * ((self.counter * 8) + 6))
        self.data = self.f.read(4 * 511)
        self.data = struct.unpack('511i', self.data)
        self.data = list(self.data)
        self.data = np.array(self.data)[np.newaxis]
        self.data = self.data.T
        self.data3 = np.concatenate((self.data3[:, :self.counter], self.data, self.data1[:, self.counter + 1:]), axis=1)
        self.fig3.imshow(self.data3)

        self.f.seek(36 + 2080 * ((self.counter * 8) + 7))
        self.data = self.f.read(4 * 511)
        self.data = struct.unpack('511i', self.data)
        self.data = list(self.data)
        self.data = np.array(self.data)[np.newaxis]
        self.data = self.data.T
        self.data4 = np.concatenate((self.data4[:, :self.counter], self.data, self.data1[:, self.counter + 1:]), axis=1)
        self.fig4.imshow(self.data4)

        self.canvas.show()
        self.counter = self.counter + 1
        if self.counter == 100:
            self.counter = 0

    def Exit(self, evt):
        self.Run = False

    def Update(self):
        while self.Run:
            app.newtime()
            app.newdataplot()
            root.update()


root = Tk()

app = App(root)
print('start update')
app.Update()

root.destroy()
