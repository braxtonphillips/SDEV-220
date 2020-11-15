"""
Braxton Phillips
SDEV 220
Chapter 9 Exercise 9.3 
Due Nov. 14, 2020
"""

from tkinter import *


class geometricFig:
    def __init__(self):
        window = Tk()
        window.title("Geometric Figures")

        self.canvas = Canvas(window, width = 500, height = 300, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        self.v1 = StringVar()
        self.v2 = StringVar()
        rbDiam = Radiobutton(frame, text = "Diamond", command = self.processFill, variable = self.v1, value = '1')
        rbTri = Radiobutton(frame, text = "Tri", command = self.processFill, variable = self.v1, value = '2')
        cbtFill = Checkbutton(frame, text = "Fill", command = self.processFill, variable = self.v2)
        rbDiam.grid(row = 1, column = 1)
        rbTri.grid(row = 1, column = 2)
        cbtFill.grid(row = 1, column = 3)

        window.mainloop()

    def processFill(self):
        color = "white" if self.v2.get() == "0" else "black"
        if self.v1.get() == '1':
            self.canvas.delete("diam", "tri")
            self.canvas.create_polygon(150,75,225,0,300,75,225,150, tags = "diam", fill = color)
        elif self.v1.get() == '2':
            self.canvas.delete("diam", "tri")
            self.canvas.create_polygon(55, 85, 155, 85, 105, 180, 55, 85,  tags = "tri", fill = color)
        else:
            self.canvas.delete("diam", "tri")


geometricFig()