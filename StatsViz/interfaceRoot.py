import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as st
from pathlib import Path

from . import interfaceCommon
from . import interfaceScatter
from . import interfaceInterval
from . import interfaceHist
from . import rw
from . import calculation
from . import graphing


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

        self.histFrame = tk.Frame(root, borderwidth=1, relief=tk.SUNKEN)
        self.histFrame = interfaceHist.HistFrame(self.histFrame)

        

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
        fileName = filedialog.askopenfilename(title = "Select a file", filetypes = (("csv and plot files","*.csv *.plot"),))

        if Path(fileName).is_file():

            if fileName[len(fileName)-3:len(fileName)] == "csv":

                self.commonFrame.selectedFileVar.set(fileName)
                self.commonFrame.selectedFile.xview_moveto(1)

                self.data, inconsistentCell = rw.read(fileName)

                if inconsistentCell != None:
                    messagebox.showinfo("Warning", "The data at row "+str(inconsistentCell[0])+" is inconsistent with the rest of the data in column "
                                        +str(inconsistentCell[1])+". The dataset may not plot properly")

                self.columnLabels = calculation.popLabels(data=self.data)

                self.scatterFrame.setFrame(self.columnLabels, self.data)
                self.intervalFrame.setFrame(self.columnLabels, self.data)
                self.histFrame.setFrame(self.columnLabels, self.data)

            else:
                graphing.figureFromFile(fileName, show=True)


#function to show options for selected graph type
#====================================================================
    def graphOptionSelected(self, event):

        if( not Path(self.commonFrame.selectedFileVar.get()).is_file()):
            messagebox.showinfo("Error", "Please select a file first")
            self.commonFrame.graphType.set("Select Graph Type")
            return

        if self.commonFrame.graphType.get() == "Scatterplot":
            self.intervalFrame.frame.grid_remove()
            self.histFrame.frame.grid_remove()
            self.scatterFrame.frame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        elif self.commonFrame.graphType.get() == "Interval Plot":
            self.scatterFrame.frame.grid_remove()
            self.histFrame.frame.grid_remove()
            self.intervalFrame.frame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")
        elif self.commonFrame.graphType.get() == "Histogram":
            self.scatterFrame.frame.grid_remove()
            self.intervalFrame.frame.grid_remove()
            self.histFrame.frame.grid(row=2, column=0, padx=3, pady=3, sticky="EW")