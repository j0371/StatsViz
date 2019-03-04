from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as st
from pathlib import Path

import rw
import calculation
import graphing


class MainWindow:

#initializer function
    def __init__(self, root):

#Root modifcations
#====================================================================
        self.root = root
        root.title("Data Visualizer")
        root.grid_columnconfigure(0, weight=1)
        root.geometry("325x265")

#Frames
#====================================================================
        self.mainFrame = Frame(root, borderwidth=1, relief=SUNKEN)
        self.mainFrame.grid(row=0,column=0, padx=3, pady=3, sticky="EW")
        
        self.scatterFrame = Frame(root, borderwidth=1, relief=SUNKEN)

        self.intervalFrame = Frame(root, borderwidth=1, relief=SUNKEN)


#====================================================================
#==============================Main Frame============================
#====================================================================

        self.graphType = StringVar()
        self.graphType.set("Select Graph Type")

        self.selectedFileVar = StringVar()
        self.selectedFileVar.set("Selected CSV File")


#Main Frame column 0
#====================================================================
        self.fileButton = Button(self.mainFrame, text="Select File", command=self.loadFile)
        self.fileButton.grid(row=0, column=0, sticky="W", padx=(10,0), pady=(10,0))

        self.graphOptions = ttk.Combobox(self.mainFrame, textvariable=self.graphType, values=["Scatterplot", "Interval Plot"], state="readonly")
        self.graphOptions.bind("<<ComboboxSelected>>", self.graphOptionSelected)
        self.graphOptions.grid(row=2, column=0, columnspan=2, padx=(10,0), pady=5, sticky="W")


#Main Frame column 1
#====================================================================
        self.selectedFile = Entry(self.mainFrame, textvariable=self.selectedFileVar, state="readonly", width=39)
        self.selectedFile.grid(row=0, column=1, padx=(3,0), pady=(10,0))

        self.selectedFileScroll = Scrollbar(self.mainFrame, orient="horizontal", command=self.selectedFile.xview)
        self.selectedFileScroll.grid(row=1,column=1,sticky="ew", pady=(0,10))

        self.selectedFile.config(xscrollcommand=self.selectedFileScroll.set)


#====================================================================
#=============================Scatter Frame==========================
#====================================================================

        self.SxVarSelection = StringVar()
        self.SyVarSelection = StringVar()
        self.ScVarSelection = StringVar()
        

#Scatter Frame column 0
#====================================================================

        self.SxVarLabel = Label(self.scatterFrame, text="X Axis Column")
        self.SxVarLabel.grid(row=0, column=0)

        self.SxVar = ttk.Combobox(self.scatterFrame, textvariable=self.SxVarSelection, values=[], state="readonly")
        self.SxVar.grid(row=1, column=0)

        self.SyVarLabel = Label(self.scatterFrame, text="Y Axis Column")
        self.SyVarLabel.grid(row=2, column=0)

        self.SyVar = ttk.Combobox(self.scatterFrame, textvariable=self.SyVarSelection, values=[], state="readonly")
        self.SyVar.grid(row=3, column=0)

        self.ScVarLabel = Label(self.scatterFrame, text="Category Column")
        self.ScVarLabel.grid(row=4, column=0)

        self.ScVar = ttk.Combobox(self.scatterFrame, textvariable=self.ScVarSelection, values=[], state="readonly")
        self.ScVar.grid(row=5, column=0)

        self.sButton = Button(self.scatterFrame, text="Create Scatterplot", command=self.createScatter)
        self.sButton.grid(row=6, column=0, columnspan=2, pady=10)

#Scatter Frame column 1
#====================================================================

        self.scatterFrame.grid_columnconfigure(0, pad=25)
        self.scatterFrame.grid_columnconfigure(1, pad=25)

        self.titleText = Label(self.scatterFrame, text="Graph Title")
        self.titleText.grid(row=0, column=1)

        self.Stitle = Entry(self.scatterFrame)
        self.Stitle.grid(row=1, column=1)

        self.xLabelText = Label(self.scatterFrame, text="X-Axis Label")
        self.xLabelText.grid(row=2, column=1)

        self.SxLabel = Entry(self.scatterFrame)
        self.SxLabel.grid(row=3, column=1)

        self.yLabelText = Label(self.scatterFrame, text="Y-Axis Label")
        self.yLabelText.grid(row=4, column=1)

        self.SyLabel = Entry(self.scatterFrame)
        self.SyLabel.grid(row=5, column=1)

#====================================================================
#=========================Interval Plot Frame========================
#====================================================================

        self.intervalLabel = Label(self.intervalFrame, text="Interval Plot Label")
        self.intervalLabel.grid(row=0,column=0)


#====================================================================
#============================Functions===============================
#====================================================================


#function to prompt file selection dialogue and load file
#====================================================================
    def loadFile(self):

        #fileName = "..\sampleData\weight-height(edited).csv"
        fileName = filedialog.askopenfilename(initialdir = "./",title = "Select a file", filetypes = (("CSV files","*.csv"),))
        self.selectedFileVar.set(fileName)
        self.selectedFile.xview_moveto(1)
        self.data = rw.read(fileName)

        self.columnLabels = calculation.shaveLabels(data=self.data)

        self.SxVar.config(values=self.columnLabels)
        self.SyVar.config(values=self.columnLabels)
        self.ScVar.config(values=["No Categories"]+self.columnLabels)

        self.SxVarSelection.set("Select a Column")
        self.SyVarSelection.set("Select a Column")
        self.ScVarSelection.set("No Categories")

        self.SxLabel.delete(0, END)
        self.SyLabel.delete(0, END)
        self.Stitle.delete(0, END)





#function to show options for selected graph type
#====================================================================
    def graphOptionSelected(self, event):

        if( not Path(self.selectedFileVar.get()).is_file()):
            messagebox.showinfo("Error", "Please select a file first")
            self.graphType.set("Select Graph Type")
            return

        if self.graphType.get() == "Scatterplot":
            self.intervalFrame.grid_remove()
            self.scatterFrame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        elif self.graphType.get() == "Interval Plot":
            self.scatterFrame.grid_remove()
            self.intervalFrame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        else:
            self.intervalFrame.grid_remove()
            self.scatterFrame.grid_remove()


#function to create the graph
#====================================================================
    def createScatter(self):

        if(self.SxVar.current() == (-1) or self.SyVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select an X and Y axis column")
            return

        if(self.SxLabel.get() == ""):
            self.SxLabel.insert(0, self.columnLabels[self.SxVar.current()])
        if(self.SyLabel.get() == ""):
            self.SyLabel.insert(0, self.columnLabels[self.SyVar.current()])
        if(self.Stitle.get() == ""):
            self.Stitle.insert(0, self.columnLabels[self.SxVar.current()] + " VS " + self.columnLabels[self.SyVar.current()])

        self.graphData = calculation.getColumns(data=self.data, xCol=self.SxVar.current(), yCol=self.SyVar.current(), groups =[self.ScVar.current()-1])

        graphing.graphScatter(xs=self.graphData[0], ys=self.graphData[1], groups=self.graphData[2], xLabel=self.SxLabel.get(), yLabel=self.SyLabel.get(), title=self.Stitle.get())