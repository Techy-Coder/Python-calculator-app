# Importing the required modules
from tkinter import *
from tkinter import font
import tkinter as tk

# Creating the main widget
root = Tk()
root.geometry("350x550+300+300")
root.title("Calculator - By Nishanth")
root.iconbitmap("img/logo.ico")
root.resizable(False, False)

# Functions
# Updating the text
val = ""
def clicked(num):
    global val
    val = val + str(num)
    data.set(val)
def clear():
    global val
    val = ""
    data.set(val)
# Solving the equation
def equal_to():
    question = data.get()
    global val
    if question:
        val = str(eval(str(question)))
    else:
        val = "No numbers entered"
    data.set(val)
# Delete function
def delete():
    txt = data.get()
    txt = list(txt)
    txt.pop()
    txt = ''.join(txt)
    global  val
    val = txt
    data.set(val)

# Creating the result frame
data = StringVar()
result_frame = Label(root, text="", anchor=SE, background = "#dadada", font = ('Verendana', 22), textvariable = data)
result_frame.pack(
    expand=True,
    fill="both"
)

# Creating the button rows
btn_row0 = Frame(root, bg="white")
btn_row0.pack(
    expand=True,
    fill="both"
)
btn_row1 = Frame(root, bg="white")
btn_row1.pack(
    expand=True,
    fill="both"
)
btn_row2 = Frame(root, bg="white")
btn_row2.pack(
    expand=True,
    fill="both"
)
btn_row3 = Frame(root, bg="white")
btn_row3.pack(
    expand=True,
    fill="both"
)
btn_row4 = Frame(root, bg="white")
btn_row4.pack(
    expand=True,
    fill="both"
)

# Creating the buttons
btn_1 = Button(
    btn_row3,
    text="1",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(1)
)
btn_1.pack(side = LEFT, expand = True, fill = "both")

btn_2 = Button(
    btn_row3,
    text="2",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(2)
)
btn_2.pack(side = LEFT, expand = True, fill = "both")

btn_3 = Button(
    btn_row3,
    text="3",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(3)
)
btn_3.pack(side = LEFT, expand = True, fill = "both")

btn_plus = Button(
    btn_row3,
    text="+",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked("+")
)
btn_plus.pack(side = LEFT, expand = True, fill = "both")

btn_4 = Button(
    btn_row2,
    text="4",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(4)
)
btn_4.pack(side = LEFT, expand = True, fill = "both")

btn_5 = Button(
    btn_row2,
    text="5",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(5)
)
btn_5.pack(side = LEFT, expand = True, fill = "both")

btn_6 = Button(
    btn_row2,
    text="6",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(6)
)
btn_6.pack(side = LEFT, expand = True, fill = "both")

btn_minus = Button(
    btn_row2,
    text="-",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked("-")
)
btn_minus.pack(side = LEFT, expand = True, fill = "both")

btn_7 = Button(
    btn_row1,
    text="7",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(7)
)
btn_7.pack(side = LEFT, expand = True, fill = "both")

btn_8 = Button(
    btn_row1,
    text="8",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(8)
)
btn_8.pack(side = LEFT, expand = True, fill = "both")

btn_9 = Button(
    btn_row1,
    text="9",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(9)
)
btn_9.pack(side = LEFT, expand = True, fill = "both")

btn_mult = Button(
    btn_row1,
    text="*",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked("*")
)
btn_mult.pack(side = LEFT, expand = True, fill = "both")

btn_div = Button(
    btn_row4,
    text="/",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked("/")
)
btn_div.pack(side = LEFT, expand = True, fill = "both")

btn_0 = Button(
    btn_row4,
    text="0",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=lambda: clicked(0)
)
btn_0.pack(side = LEFT, expand = True, fill = "both")

btn_equal = Button(
    btn_row4,
    text="=",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=equal_to
)
btn_equal.pack(side = LEFT, expand = True, fill = "both")

btn_clear = Button(
    btn_row0,
    text="C",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=clear
)
btn_clear.pack(side = LEFT, expand = True, fill = "both")

btn_del = Button(
    btn_row0,
    text="Del",
    font = (
        "Verendana",
        22
    ),
    relief=GROOVE,
    border = 0,
    command=delete
)
btn_del.pack(side = LEFT, expand = True, fill = "both")

# Running the app
root.mainloop()