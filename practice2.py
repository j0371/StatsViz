import matplotlib.pyplot as mplot
import numpy
import scipy.stats as stats
from tkinter import filedialog
from tkinter import *

root = Tk()

button = Button(root, text="button")
button.pack()

check = Checkbutton(root)
check.pack()

entry = Entry(root)
entry.pack()

label = Label(root, text="label")
label.pack()

listbox = Listbox(root, selectmode="multiple")
listbox.insert(END, "column 1")
listbox.insert(END, "column 2")
listbox.pack()

#menu

msg = Message(root, text="message")
msg.pack()

radio = Radiobutton(root)
radio.pack()

scale = Scale(root)
scale.pack()

#scrollbar

text = Text(root)
text.insert(INSERT, "text")
text.pack()

spin = Spinbox(root)
spin.pack()

labelframe = LabelFrame(root, text="LabelFrame")
labelframe.pack(fill="both", expand="yes")
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()