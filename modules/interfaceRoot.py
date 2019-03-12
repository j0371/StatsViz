import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as st
from pathlib import Path

import interfaceCommon
import interfaceScatter
import interfaceInterval
import rw
import calculation
import graphing


class RootWindow:

#initializer function
    def __init__(self, root):

#Root modifcations
#====================================================================
        self.root = root
        root.title("Data Visualizer")
        root.grid_columnconfigure(0, weight=1)
        #root.geometry("343x282")                       #!!!SET TO NEW DIMENSIONS!!!#

#Frames
#====================================================================
        self.commonFrame = tk.Frame(root, borderwidth=1, relief=tk.SUNKEN)
        self.commonFrame = interfaceCommon.CommonFrame(self.commonFrame)
        
        self.scatterFrame = tk.Frame(root, borderwidth=1, relief=tk.SUNKEN)
        self.scatterFrame = interfaceScatter.ScatterFrame(self.scatterFrame)

        self.intervalFrame = tk.Frame(root, borderwidth=1, relief=tk.SUNKEN)

#Event Bindings
#====================================================================
        self.commonFrame.fileButton.bind("<Button-1>", self.loadFile)
        self.commonFrame.graphOptions.bind("<<ComboboxSelected>>", self.graphOptionSelected)

        self.scatterFrame.sButton.bind("<Button-1>", self.createScatter)



#====================================================================
#============================Functions===============================
#====================================================================


#function to prompt file selection dialogue and load file
#====================================================================
    def loadFile(self, event):

        try:
            #fileName = "..\sampleData\weight-height(edited).csv"
            fileName = filedialog.askopenfilename(initialdir = "./",title = "Select a file", filetypes = (("CSV files","*.csv"),))
        except:
            pass

        self.commonFrame.selectedFileVar.set(fileName)
        self.commonFrame.selectedFile.xview_moveto(1)

        self.data = rw.read(fileName)

        self.columnLabels = calculation.shaveLabels(data=self.data)

        self.scatterFrame.xVar.config(values=self.columnLabels)
        self.scatterFrame.yVar.config(values=self.columnLabels)
        self.scatterFrame.cVar.config(values=["No Categories"]+self.columnLabels)

        self.scatterFrame.xVarSelection.set("Select a Column")
        self.scatterFrame.yVarSelection.set("Select a Column")
        self.scatterFrame.cVarSelection.set("No Categories")

        self.scatterFrame.xLabel.delete(0, tk.END)
        self.scatterFrame.yLabel.delete(0, tk.END)
        self.scatterFrame.title.delete(0, tk.END)

        self.scatterFrame.xGridCheckVal.set("")
        self.scatterFrame.yGridCheckVal.set("")



#function to show options for selected graph type
#====================================================================
    def graphOptionSelected(self, event):

        if( not Path(self.commonFrame.selectedFileVar.get()).is_file()):
            messagebox.showinfo("Error", "Please select a file first")
            self.commonFrame.graphType.set("Select Graph Type")
            return

        if self.commonFrame.graphType.get() == "Scatterplot":
            self.intervalFrame.grid_remove()
            self.scatterFrame.frame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        elif self.commonFrame.graphType.get() == "Interval Plot":
            self.scatterFrame.frame.grid_remove()
            self.intervalFrame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        else:
            self.intervalFrame.grid_remove()
            self.scatterFrame.grid_remove()


#function to create the graph
#====================================================================
    def createScatter(self, event):

        if(self.scatterFrame.xVar.current() == (-1) or self.scatterFrame.yVar.current() == (-1)):
            messagebox.showinfo("Error", "Please select an X and Y axis column")
            return

        if(self.scatterFrame.xLabel.get() == ""):
            self.scatterFrame.xLabel.insert(0, self.columnLabels[self.scatterFrame.xVar.current()])
        if(self.scatterFrame.yLabel.get() == ""):
            self.scatterFrame.yLabel.insert(0, self.columnLabels[self.scatterFrame.yVar.current()])
        if(self.scatterFrame.title.get() == ""):
            self.scatterFrame.title.insert(0, self.columnLabels[self.scatterFrame.xVar.current()] + " VS " + self.columnLabels[self.scatterFrame.yVar.current()])

        self.graphData = calculation.getColumns(data=self.data, xCol=self.scatterFrame.xVar.current(),
                                                yCol=self.scatterFrame.yVar.current(), groups =[self.scatterFrame.cVar.current()-1])

        graphing.graphScatter(xs=self.graphData[0], ys=self.graphData[1], groups=self.graphData[2], xLabel=self.scatterFrame.xLabel.get(),
                              yLabel=self.scatterFrame.yLabel.get(), title=self.scatterFrame.title.get(), gridLines=self.scatterFrame.xGridCheckVal.get()+self.scatterFrame.yGridCheckVal.get())