from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import pallet

root = Tk()
root.title("Board")
root.geometry("1050x570+150+50")
root.configure(bg="#a47551")
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'


def locate_xy(work):
    global current_x, current_y
    canvas.bind('<B1-Motion>', addLine)
    current_x = work.x
    current_y = work.y


def addLine(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(),
                       fill=color, capstyle=ROUND, smooth=TRUE)
    current_x, current_y = work.x, work.y


def show_color(new_color):
    global color
    color = new_color


def new_canvas():
    canvas.delete('all')
    pallet.display_pallet(colors, show_color)


def Erase():
    global color
    color = 'white'


colors = Canvas(root, bg="#eed6d3", width=280, height=37, bd=0)
colors.place(x=375, y=500)
myFont = font.Font(family='Cuckoo', size = 10, weight='bold')
Button(root, text="Erase All", bg="#d0b49f",font = myFont, command=new_canvas).place(x=250, y=500)
Button(root, text="Eraser", bg="#d0b49f", font = myFont,
       command=Erase).place(x=170, y=500)
canvas = Canvas(root, width=930, height=425, background="white", cursor="hand2")

canvas.place(x=60, y=40)

pallet.display_pallet(colors, show_color)


canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=480)
value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=500)
text = "Done by Kharkivskyi Yuriy\nFor HNEU"
label2 = Label(text=text, justify=LEFT, font = myFont)
label2.place(x = 750,y = 500)
root.mainloop()