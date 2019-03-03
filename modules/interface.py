from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.scrolledtext as st
import rw
import calculation


class MainWindow:

#initializer function
    def __init__(self, root):

#Root modifcations
#====================================================================  
        root.title("Data Visualizer")

        root.grid_columnconfigure(0, weight=1)

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


#Main Frame column 0
#====================================================================
        self.fileButton = Button(self.mainFrame, text="Select File", command=self.loadFile)
        self.fileButton.grid(row=0, column=0, sticky="W", padx=(10,0), pady=10)

        self.graphOptions = ttk.Combobox(self.mainFrame, textvariable=self.graphType, values=["Scatterplot", "Interval Plot"], state="readonly")
        self.graphOptions.bind("<<ComboboxSelected>>", self.graphOptionSelected)
        self.graphOptions.grid(row=1, column=0, columnspan=2, padx=(10,0), pady=5, sticky="W")


#Main Frame column 1
#====================================================================
        self.selectedFile = Label(self.mainFrame, text="Selected CSV File")
        self.selectedFile.grid(row=0, column=1, sticky="W", padx=(3,0), pady=10)


#====================================================================
#=============================Scatter Frame==========================
#====================================================================

        self.SxVarSelection = StringVar()
        self.SxVarSelection.set("X Variable Column")

        self.SyVarSelection = StringVar()
        self.SyVarSelection.set("Y Variable Column")

        self.ScVarSelection = StringVar()
        self.ScVarSelection.set("Category Column")

#Scatter Frame column 0
#====================================================================
        self.SxVar = ttk.Combobox(self.scatterFrame, textvariable=self.SxVarSelection, values=[], state="readonly")
        self.SxVar.grid(row=1, column=0)

        self.SyVar = ttk.Combobox(self.scatterFrame, textvariable=self.SyVarSelection, values=[], state="readonly")
        self.SyVar.grid(row=3, column=0)

        self.ScVar = ttk.Combobox(self.scatterFrame, textvariable=self.ScVarSelection, values=["No Categories"], state="readonly")
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

        fileName = filedialog.askopenfilename(initialdir = "./",title = "Select a file", filetypes = (("CSV files","*.csv"),))
        self.selectedFile.config(text=fileName)
        self.data = rw.read(fileName)


#function to show options for selected graph type
#====================================================================
    def graphOptionSelected(self, event):

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
        print("Plot will be created")