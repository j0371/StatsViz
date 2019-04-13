import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from . import rw
from . import calculation
from . import graphing

class HistFrame:

    def __init__(self, frame):

        self.frame = frame

        self.xVarSelection = tk.StringVar()
        self.binTypeSelection = tk.StringVar()
        self.binNumSelection = tk.StringVar()
        
        self.xGridCheckVal = tk.StringVar()
        self.yGridCheckVal = tk.StringVar()

        #Column 0
#====================================================================

        frame.grid_columnconfigure(0, pad=25)

        self.xVarLabel = tk.Label(frame, text="X-Axis Column *")
        self.xVarLabel.grid(row=0, column=0)

        self.xVar = ttk.Combobox(frame, textvariable=self.xVarSelection, values=[], state="readonly")
        self.xVar.grid(row=1, column=0)

        self.binTypeLabel = tk.Label(frame, text="Bin Type")
        self.binTypeLabel.grid(row=2, column=0)

        self.binType = ttk.Combobox(frame, textvariable=self.binTypeSelection, values=["Automatic","Manual"], state="readonly")
        self.binType.bind("<<ComboboxSelected>>", self.binTypeSelected)
        self.binType.grid(row=3, column=0)

        self.binNumLabel = tk.Label(frame, text="Number of bins")
        self.binNumLabel.grid(row=4, column=0)

        vcmd = (frame.register(self.validate))
        self.binNum = tk.Entry(frame, textvariable=self.binNumSelection, width=23, validate="all", validatecommand=(vcmd, "%P"))
        self.binNum.grid(row=5, column=0)

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

        self.graphButton = tk.Button(frame, text="Create Histogram", command=self.createHist)
        self.graphButton.grid(row=6, column=1, pady=(10,1))

        self.saveButton = tk.Button(frame, text=" Save Histogram ", command=self.saveHist)
        self.saveButton.grid(row=7, column=1)

#====================================================================
#============================Functions===============================
#====================================================================

    def setFrame(self, columnLabels: list, data: list):
        
        self.columnLabels = columnLabels
        self.data = data

        self.xVar.config(values=columnLabels)

        self.xVarSelection.set("Select a Column")
        self.binType.set("Automatic")

        self.xLabel.delete(0, tk.END)
        self.yLabel.delete(0, tk.END)
        self.title.delete(0, tk.END)

        self.binNumLabel["state"] = "disabled"
        self.binNum["state"] = "disabled"

        self.xGridCheckVal.set("")
        self.yGridCheckVal.set("")

#validation function for the bin number entry
    def validate(self, P):
            if(str.isdigit(P)):
                if(len(self.binNum.get()) == 0 and int(P) > 0):
                    return True
                elif(len(self.binNum.get()) != 0):
                    return True
                else:
                    return False
            elif(P == ""):
                return True
            else:
                return False

#event handler when the bintype changes, disables/enables bin number
    def binTypeSelected(self, event):

        if self.binTypeSelection.get() == "Automatic":
            self.binNumLabel["state"] = "disabled"
            self.binNum["state"] = "disabled"
            self.binNumSelection.set("")
        elif self.binTypeSelection.get() == "Manual":
            self.binNumLabel["state"] = "normal"
            self.binNum["state"] = "normal"

#event handler that uses the gui specified data to create a histogram
    def createHist(self):
        
        if(self.xVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select a column for the X-axis")
            return

        if(self.xLabel.get() == ""):
            xLabel = self.columnLabels[self.xVar.current()]
        else:
            xLabel = self.xLabel.get()
        if(self.yLabel.get() == ""):
            yLabel = "Count"
        else:
            yLabel = self.yLabel.get()
        if(self.title.get() == ""):
            title = ("Histogram of " + self.columnLabels[self.xVar.current()])
        else:
            title = self.title.get()

        graphData = calculation.getColumns(data=self.data, xCol=self.xVar.current())

        if(self.binNumSelection.get() != ""):
            bins = int(self.binNumSelection.get())
        else:
            bins = None

        graphing.graphHist(xs=graphData[0], bins=bins, xLabel=xLabel,
                              yLabel=yLabel, title=title, gridLines=self.xGridCheckVal.get()+self.yGridCheckVal.get(), show = True)
        

#event handler that prompts the user to save the histogram to a file
    def saveHist(self):
        
        if(self.xVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select a column for the X-axis")
            return

        if(self.xLabel.get() == ""):
            xLabel = self.columnLabels[self.xVar.current()]
        else:
            xLabel = self.xLabel.get()
        if(self.yLabel.get() == ""):
            yLabel = "Count"
        else:
            yLabel = self.yLabel.get()
        if(self.title.get() == ""):
            title = ("Histogram of " + self.columnLabels[self.xVar.current()])
        else:
            title = self.title.get()

        graphData = calculation.getColumns(data=self.data, xCol=self.xVar.current())

        if(self.binNumSelection.get() != ""):
            bins = int(self.binNumSelection.get())
        else:
            bins = None

        fileName = filedialog.asksaveasfilename(title = "Save File", defaultextension=".plot")

        if fileName != "":
            rw.saveHist(xs=graphData[0], bins=bins, xLabel=xLabel,
                                yLabel=yLabel, title=title, gridLines=self.xGridCheckVal.get()+self.yGridCheckVal.get(), fileName=fileName)