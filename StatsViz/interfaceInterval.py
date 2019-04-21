import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

from . import rw
from . import calculation
from . import graphing

class IntervalFrame:

    def __init__(self, frame):

        self.frame = frame

        self.iTypeSelection = tk.StringVar()

        self.yVarSelection = tk.StringVar()

        self.colorCatSelection = tk.StringVar()

        self.xGridCheckVal = tk.StringVar()
        self.yGridCheckVal = tk.StringVar()
        

#Column 0
#====================================================================

        frame.grid_columnconfigure(0, pad=25)

        self.cVarLabel = tk.Label(frame, text="X-Axis Columns")
        self.cVarLabel.grid(row=3, column=0)

        self.cVar = tk.Listbox(frame, height=4, width=23)
        self.cVar.grid(row=4, column=0, rowspan=3)

        self.yVarLabel = tk.Label(frame, text="Y-Axis Column *")
        self.yVarLabel.grid(row=7, column=0, pady=(5,0))

        self.yVar = ttk.Combobox(frame, textvariable=self.yVarSelection, values=[], state="readonly")
        self.yVar.grid(row=8, column=0)

        self.colorCatLabel = tk.Label(frame, text="Color Category Column")
        self.colorCatLabel.grid(row=9, column=0, pady=(5,0))

        self.colorCat = ttk.Combobox(frame, textvariable=self.colorCatSelection, values=[], state="readonly")
        self.colorCat.grid(row=10, column=0)




#Column 1
#====================================================================

        self.deselectButton = tk.Button(frame, text="⤺")
        self.deselectButton["font"] = font.Font(size=12)
        self.deselectButton.bind("<Button-1>", self.removeCategory)
        self.deselectButton.grid(row=4, column=1)

        self.selectButton = tk.Button(frame, text="⤻")
        self.selectButton["font"] = font.Font(size=12)
        self.selectButton.bind("<Button-1>", self.addCategory)
        self.selectButton.grid(row=6, column=1)

#Column 2
#====================================================================

        frame.grid_columnconfigure(2, pad=25)

        self.iTypeLabel = tk.Label(frame, text="Interval Type *")
        self.iTypeLabel.grid(row=0, column=2)

        self.iType = ttk.Combobox(frame, textvariable=self.iTypeSelection, values=["Standard Error","Standard Deviation","Confidence Interval"], state="readonly")
        self.iType.grid(row=1, column=2, pady=(0,5))

        self.cVarSelectedLabel = tk.Label(frame, text="Selected X-Axis Columns\n(Outermost first)")
        self.cVarSelectedLabel.grid(row=2, column=2, rowspan=2)

        self.cVarSelected = tk.Listbox(frame, height=4, width=23)
        self.cVarSelected.grid(row=4, column=2, rowspan=3)

        self.xGridCheck = tk.Checkbutton(frame, variable=self.xGridCheckVal, onvalue="x", offvalue="", text="X-axis grid lines")
        self.xGridCheck.grid(row=8, column=2)

        self.yGridCheck = tk.Checkbutton(frame, variable=self.yGridCheckVal, onvalue="y", offvalue="", text="Y-axis grid lines")
        self.yGridCheck.grid(row=9, column=2)

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

        self.graphButton = tk.Button(frame, text="Create Interval Plot", command=self.createInterval)
        self.graphButton.grid(row=9, column=3, rowspan=2, pady=(10,1))

        self.saveButton = tk.Button(frame, text=" Save Interval Plot ", command=self.saveInterval)
        self.saveButton.grid(row=11, column=3)



#====================================================================
#============================Functions===============================
#====================================================================


#code that sets the up the data to view for the interval frame
    def setFrame(self, columnLabels: list, data: list):

        self.columnLabels = columnLabels
        self.data = data

        yLabels = []

        for i in range(len(columnLabels)):
            try:
                float(data[0][i])
                yLabels.append(columnLabels[i])
            except:
                pass

        
        self.yVar.config(values=yLabels)

        self.cVar.delete(0, tk.END)
        self.cVarSelected.delete(0, tk.END)

        for label in columnLabels:
            self.cVar.insert("end", label)

        self.yVarSelection.set("Select a Column")

        self.colorCat.config(values=["No Color Categories"])
        self.colorCatSelection.set("No Color Categories")

        self.iTypeSelection.set("Select Type")

        self.xLabel.delete(0, tk.END)
        self.yLabel.delete(0, tk.END)
        self.title.delete(0, tk.END)

        self.xGridCheckVal.set("")
        self.yGridCheckVal.set("")

    def addCategory(self, event):

        if self.cVar.curselection():
            selectedIndex = self.cVar.curselection()[0]
            selectedValue = self.cVar.get(selectedIndex)

            self.cVarSelected.insert(tk.END, selectedValue)
            self.cVar.delete(selectedIndex)

            categories = []

            for _, listbox_entry in enumerate(self.cVarSelected.get(0, tk.END)):
                categories.append(listbox_entry)

            self.colorCat.config(values=["No Color Categories"]+categories)
            self.colorCatSelection.set("No Color Categories")

    def removeCategory(self, event):

        if self.cVarSelected.curselection():
            selectedIndex = self.cVarSelected.curselection()[0]
            selectedValue = self.cVarSelected.get(selectedIndex)

            self.cVar.insert(self.columnLabels.index(selectedValue), selectedValue)
            self.cVarSelected.delete(selectedIndex)

            categories = []

            for _, listbox_entry in enumerate(self.cVarSelected.get(0, tk.END)):
                categories.append(listbox_entry)

            self.colorCat.config(values=["No Color Categories"]+categories)
            self.colorCatSelection.set("No Color Categories")

    def createInterval(self):

        if(self.iType.current() == (-1)):
            messagebox.showinfo("Error", "Please select an interval type")
            return
        elif(self.yVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select a column for the Y-axis")
            return

        if(self.yLabel.get() == ""):
            yLabel = self.yVarSelection.get()
        else:
            yLabel = self.yLabel.get()
        if(self.title.get() == ""):
            title = self.iTypeSelection.get() + " of " + self.yVarSelection.get()
        else:
            title = self.title.get()
        if(self.xLabel.get() == "" and len(self.cVarSelected.get(0, tk.END)) == 1):
            xLabel = self.cVarSelected.get(0)
        else:
            xLabel = self.xLabel.get()

        typeParam = ""

        if(self.iType.current() == 0):
            typeParam = "se"
        elif(self.iType.current() == 1):
            typeParam = "sd"
        elif(self.iType.current() == 2):
            typeParam = "ci"


        cVals = self.cVarSelected.get(0, tk.END)
        cIndices = []

        if len(cVals) > 0:
            for val in cVals:
                cIndices.append(self.columnLabels.index(val))
        else:
            cIndices = None

        colorCatIndex = None

        if (self.colorCatSelection.get() != "No Color Categories"):
            colorCatIndex = self.colorCat.current()-1

        rawGraphData = calculation.getColumns(data=self.data,
                                           yCol=self.columnLabels.index(self.yVarSelection.get()), groups=cIndices)

        graphData = calculation.getIntervals(type=typeParam, ys=rawGraphData[1], groups=rawGraphData[2])

        graphing.graphInterval(data=graphData, title=title, xLabel=xLabel,
                                yLabel=yLabel, gridLines=self.xGridCheckVal.get()+self.yGridCheckVal.get(), groupNames=cVals, colorIndex=colorCatIndex, show=True)

    def saveInterval(self):
        
        if(self.iType.current() == (-1)):
            messagebox.showinfo("Error", "Please select an interval type")
            return
        elif(self.yVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select a column for the Y-axis")
            return

        if(self.yLabel.get() == ""):
            yLabel = self.yVarSelection.get()
        else:
            yLabel = self.yLabel.get()
        if(self.title.get() == ""):
            title = self.iTypeSelection.get() + " of " + self.yVarSelection.get()
        else:
            title = self.title.get()
        if(self.xLabel.get() == "" and len(self.cVarSelected.get(0, tk.END)) == 1):
            xLabel = self.cVarSelected.get(0)
        else:
            xLabel = self.xLabel.get()

        typeParam = ""

        if(self.iType.current() == 0):
            typeParam = "se"
        elif(self.iType.current() == 1):
            typeParam = "sd"
        elif(self.iType.current() == 2):
            typeParam = "ci"


        cVals = self.cVarSelected.get(0, tk.END)
        cIndices = []

        if len(cVals) > 0:
            for val in cVals:
                cIndices.append(self.columnLabels.index(val))
        else:
            cIndices = None

        colorCatIndex = None

        if (self.colorCatSelection.get() != "No Color Categories"):
            colorCatIndex = self.colorCat.current()-1

        rawGraphData = calculation.getColumns(data=self.data,
                                           yCol=self.columnLabels.index(self.yVarSelection.get()), groups=cIndices)

        graphData = calculation.getIntervals(type=typeParam, ys=rawGraphData[1], groups=rawGraphData[2])

        fileName = filedialog.asksaveasfilename(title = "Save File", defaultextension=".plot")

        if fileName != "":
            rw.saveInterval(data=graphData, title=title, xLabel=xLabel,
                                    yLabel=yLabel, gridLines=self.xGridCheckVal.get()+self.yGridCheckVal.get(), groupNames=cVals, colorIndex=colorCatIndex, fileName=fileName)