import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import calculation
import graphing

class ScatterFrame:

    def __init__(self, frame):

        self.frame = frame

        self.xVarSelection = tk.StringVar()
        self.yVarSelection = tk.StringVar()
        self.cVarSelection = tk.StringVar()

        self.xGridCheckVal = tk.StringVar()
        self.yGridCheckVal = tk.StringVar()
        

#Column 0
#====================================================================

        frame.grid_columnconfigure(0, pad=25)

        self.xVarLabel = tk.Label(frame, text="X-Axis Column")
        self.xVarLabel.grid(row=0, column=0)

        self.xVar = ttk.Combobox(frame, textvariable=self.xVarSelection, values=[], state="readonly")
        self.xVar.grid(row=1, column=0)

        self.yVarLabel = tk.Label(frame, text="Y-Axis Column")
        self.yVarLabel.grid(row=2, column=0)

        self.yVar = ttk.Combobox(frame, textvariable=self.yVarSelection, values=[], state="readonly")
        self.yVar.grid(row=3, column=0)

        self.cVarLabel = tk.Label(frame, text="Category Column")
        self.cVarLabel.grid(row=4, column=0)

        self.cVar = ttk.Combobox(frame, textvariable=self.cVarSelection, values=[], state="readonly")
        self.cVar.grid(row=5, column=0)

        self.xGridCheck = tk.Checkbutton(frame, variable=self.xGridCheckVal, onvalue="x", offvalue="", text="X-axis grid lines")
        self.xGridCheck.grid(row=6, column=0)

        self.yGridCheck = tk.Checkbutton(frame, variable=self.yGridCheckVal, onvalue="y", offvalue="", text="Y-axis grid lines")
        self.yGridCheck.grid(row=7, column=0)

        

#Column 1
#====================================================================

        
        frame.grid_columnconfigure(1, pad=25)

        self.titleText = tk.Label(frame, text="Graph Title")
        self.titleText.grid(row=0, column=1)

        self.title = tk.Entry(frame, width=23)
        self.title.grid(row=1, column=1)

        self.xLabelText = tk.Label(frame, text="X-Axis Label")
        self.xLabelText.grid(row=2, column=1)

        self.xLabel = tk.Entry(frame, width=23)
        self.xLabel.grid(row=3, column=1)

        self.yLabelText = tk.Label(frame, text="Y-Axis Label")
        self.yLabelText.grid(row=4, column=1)

        self.yLabel = tk.Entry(frame, width=23)
        self.yLabel.grid(row=5, column=1)

        self.graphButton = tk.Button(frame, text="Create Scatterplot")
        self.graphButton.bind("<Button-1>", self.createScatter)
        self.graphButton.bind("<ButtonRelease-1>", self.raiseButton)
        self.graphButton.grid(row=6, column=1, rowspan=2, pady=10)

        

#====================================================================
#============================Functions===============================
#====================================================================



    def raiseButton(self, event):
        self.graphButton.config(relief=tk.RAISED)

    def setFrame(self, columnLabels: list, data: list):

        self.columnLabels = columnLabels
        self.data = data

        self.xVar.config(values=columnLabels)
        self.yVar.config(values=columnLabels)
        self.cVar.config(values=["No Categories"]+columnLabels)

        self.xVarSelection.set("Select a Column")
        self.yVarSelection.set("Select a Column")
        self.cVarSelection.set("No Categories")

        self.xLabel.delete(0, tk.END)
        self.yLabel.delete(0, tk.END)
        self.title.delete(0, tk.END)

        self.xGridCheckVal.set("")
        self.yGridCheckVal.set("")

    def createScatter(self, event):

        self.graphButton.config(relief=tk.SUNKEN)

        if(self.xVar.current() == (-1) or self.yVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select a column for the X-axis and Y-axis")
            self.graphButton.config(relief=tk.RAISED)
            return

        if(self.xLabel.get() == ""):
            self.xLabel.insert(0, self.columnLabels[self.xVar.current()])
        if(self.yLabel.get() == ""):
            self.yLabel.insert(0, self.columnLabels[self.yVar.current()])
        if(self.title.get() == ""):
            self.title.insert(0, self.columnLabels[self.xVar.current()] + " VS " + self.columnLabels[self.yVar.current()])

        graphData = calculation.getColumns(data=self.data, xCol=self.xVar.current(),
                                           yCol=self.yVar.current(), groups =[self.cVar.current()-1])

        graphing.graphScatter(xs=graphData[0], ys=graphData[1], groups=graphData[2], xLabel=self.xLabel.get(),
                              yLabel=self.yLabel.get(), title=self.title.get(), gridLines=self.xGridCheckVal.get()+self.yGridCheckVal.get())

        self.xLabel.delete(0, tk.END)
        self.yLabel.delete(0, tk.END)
        self.title.delete(0, tk.END)