import tkinter as tk
from tkinter import ttk

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

        self.xVarLabel = tk.Label(frame, text="X Axis Column")
        self.xVarLabel.grid(row=0, column=0)

        self.xVar = ttk.Combobox(frame, textvariable=self.xVarSelection, values=[], state="readonly")
        self.xVar.grid(row=1, column=0)

        self.yVarLabel = tk.Label(frame, text="Y Axis Column")
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
        self.graphButton.bind("<ButtonRelease-1>", self.raiseButton)
        self.graphButton.grid(row=6, column=1, rowspan=2, pady=10)

    def raiseButton(self, event):
        self.graphButton.config(relief=tk.RAISED)