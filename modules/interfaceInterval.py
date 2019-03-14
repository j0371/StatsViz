import tkinter as tk
from tkinter import ttk

class IntervalFrame:

    def __init__(self, frame):

        self.frame = frame

        self.iTypeSelection = tk.StringVar()
        self.iTypeSelection.set("Select Type")

        self.yVarSelection = tk.StringVar()
        #self.cVarSelection = tk.StringVar()

        self.xGridCheckVal = tk.StringVar()
        self.yGridCheckVal = tk.StringVar()
        

#Column 0
#====================================================================

        frame.grid_columnconfigure(0, pad=25)

        self.cVarLabel = tk.Label(frame, text="X-Axis Columns")
        self.cVarLabel.grid(row=3, column=0)

        self.cVar = tk.Listbox(frame, height=4, width=23)
        self.cVar.grid(row=4, column=0, rowspan=3)

        self.yVarLabel = tk.Label(frame, text="Y-Axis Column")
        self.yVarLabel.grid(row=7, column=0, columnspan=3, pady=(5,0))

        self.yVar = ttk.Combobox(frame, textvariable=self.yVarSelection, values=[], state="readonly")
        self.yVar.grid(row=8, column=0, columnspan=3)

        self.xGridCheck = tk.Checkbutton(frame, variable=self.xGridCheckVal, onvalue="x", offvalue="", text="X-axis grid lines")
        self.xGridCheck.grid(row=9, column=0, columnspan=3)

        self.yGridCheck = tk.Checkbutton(frame, variable=self.yGridCheckVal, onvalue="y", offvalue="", text="Y-axis grid lines")
        self.yGridCheck.grid(row=10, column=0, columnspan=3)


#Column 1
#====================================================================

        self.selectButton = tk.Button(frame, text="-->")
        self.selectButton.grid(row=4, column=1)

        self.deselectButton = tk.Button(frame, text="<--")
        self.deselectButton.grid(row=6, column=1)


#Column 2
#====================================================================

        frame.grid_columnconfigure(2, pad=25)

        self.iTypeLabel = tk.Label(frame, text="Interval Type")
        self.iTypeLabel.grid(row=0, column=2)

        self.iType = ttk.Combobox(frame, textvariable=self.iTypeSelection, values=["Standard Error","Standard Deviation","Confidence Interval"], state="readonly")
        self.iType.grid(row=1, column=2, pady=(0,5))

        self.cVarSelectedLabel = tk.Label(frame, text="Selected X-Axis Columns\n(Outermost first)")
        self.cVarSelectedLabel.grid(row=2, column=2, rowspan=2)

        self.cVarSelected = tk.Listbox(frame, height=4, width=23)
        self.cVarSelected.grid(row=4, column=2, rowspan=3)

#Column 3
#====================================================================
  
        frame.grid_columnconfigure(3, pad=25)

        self.titleText = tk.Label(frame, text="Graph Title")
        self.titleText.grid(row=3, column=3)

        self.title = tk.Entry(frame, width=23)
        self.title.grid(row=4, column=3)

        self.xLabelText = tk.Label(frame, text="X-Axis Label")
        self.xLabelText.grid(row=5, column=3)

        self.xLabel = tk.Entry(frame, width=23)
        self.xLabel.grid(row=6, column=3)

        self.yLabelText = tk.Label(frame, text="Y-Axis Label")
        self.yLabelText.grid(row=7, column=3)

        self.yLabel = tk.Entry(frame, width=23)
        self.yLabel.grid(row=8, column=3)

        self.graphButton = tk.Button(frame, text="Create Interval Plot")
        self.graphButton.grid(row=9, column=3, rowspan=2, pady=10)


    def setFrame(self, columnLabels: list):
        self.yVar.config(values=columnLabels)
        self.cVar.config(values=columnLabels)

        self.yVarSelection.set("Select a Column")

        self.xLabel.delete(0, tk.END)
        self.yLabel.delete(0, tk.END)
        self.title.delete(0, tk.END)

        self.xGridCheckVal.set("")
        self.yGridCheckVal.set("")