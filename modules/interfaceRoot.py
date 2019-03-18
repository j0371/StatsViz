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
        self.intervalFrame = interfaceInterval.IntervalFrame(self.intervalFrame)

#Event Bindings
#====================================================================
        self.commonFrame.fileButton.bind("<Button-1>", self.loadFile)
        self.commonFrame.graphOptions.bind("<<ComboboxSelected>>", self.graphOptionSelected)


#====================================================================
#============================Functions===============================
#====================================================================


#function to prompt file selection dialogue and load file
#====================================================================
    def loadFile(self, event):

        self.commonFrame.fileButton.config(relief=tk.SUNKEN)


        #fileName = "C:/Users/halo2_000/Desktop/StatsViz/sampleData/created.csv"
        fileName = filedialog.askopenfilename(initialdir = "./",title = "Select a file", filetypes = (("CSV files","*.csv"),))

        if Path(fileName).is_file():

            self.commonFrame.selectedFileVar.set(fileName)
            self.commonFrame.selectedFile.xview_moveto(1)

            self.data = rw.read(fileName)

            self.columnLabels = calculation.popLabels(data=self.data)

            self.scatterFrame.setFrame(self.columnLabels, self.data)
            self.intervalFrame.setFrame(self.columnLabels, self.data)


#function to show options for selected graph type
#====================================================================
    def graphOptionSelected(self, event):

        if( not Path(self.commonFrame.selectedFileVar.get()).is_file()):
            messagebox.showinfo("Error", "Please select a file first")
            self.commonFrame.graphType.set("Select Graph Type")
            return

        if self.commonFrame.graphType.get() == "Scatterplot":
            self.intervalFrame.frame.grid_remove()
            self.scatterFrame.frame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        elif self.commonFrame.graphType.get() == "Interval Plot":
            self.scatterFrame.frame.grid_remove()
            self.intervalFrame.frame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")