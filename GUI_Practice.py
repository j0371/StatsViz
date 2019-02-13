from tkinter import *
import matplotlib.pyplot as mplot

def makeScatter(event):
    fileName = entry_1.get()

    xs = []
    ys = []
    
    data = open(fileName, "r")
    data = data.read()
    data = data.split("\n")

    while (data[-1] == ""):
        data.pop()

    for i in range(0,len(data)):
        row = data[i].split(",")
        print(row[1])
        xs.append(row[1])
        ys.append(row[2])

    mplot.scatter(xs,ys,color="red")
    mplot.show()

root = Tk()

label_1 = Label(root, text="file")

entry_1 = Entry(root)

label_1.grid(row=0)
entry_1.grid(row=0,column=1)

button_1 = Button(root, text="Make Scatter")
button_1.bind("<Button-1>", makeScatter)
button_1.grid(columnspan=2)

root.mainloop()