from tkinter import *
import matplotlib.pyplot as mplot


class mainWindow:

    def __init__(self, root):


#Frames
#====================================================================
        self.mainFrame = Frame(root, borderwidth=1, relief=SUNKEN)
        self.mainFrame.grid(row=0,column=0, padx=3, pady=3)
        
        self.scatterFrame = Frame(root, borderwidth=1, relief=SUNKEN)

        self.intervalFrame = Frame(root, borderwidth=1, relief=SUNKEN)


#====================================================================
#==============================Main Frame============================
#====================================================================

        self.graphType = StringVar(root)
        self.graphType.set("Select Graph Type")


#Main Frame column 0
#====================================================================
        self.fileButton = Button(self.mainFrame, text="Select File", command=self.loadFile)
        self.fileButton.grid(row=0, column=0, sticky="W", padx=(25,0), pady=(25,0))

        self.graphOptions = OptionMenu(self.mainFrame, self.graphType, "Select Graph Type", "Scatterplot", "Interval Plot", command=self.graphOptionSelected)
        self.graphOptions.config(width=15)
        self.graphOptions.grid(row=1, column=0, columnspan=2, padx=(25,0), pady=5, sticky="W")


#Main Frame column 1
#====================================================================
        self.selectedFile = Label(self.mainFrame, text="File path of currently selected CSV")
        self.selectedFile.grid(row=0, column=1, sticky="W", padx=(3,0), pady=(25,0))


#====================================================================
#=============================Scatter Frame==========================
#====================================================================

        self.SxVarSelection = StringVar(root)
        self.SxVarSelection.set("Select X Variable Column")

#Scatter Frame column 0
#====================================================================
        self.SxVar = OptionMenu(self.scatterFrame, self.SxVarSelection, "Select X Variable Column") #!WHEN CSV IS LOADABLE, USE A LIST TO SHOW COLUMNS!
        self.SxVar.config(width=30)
        self.SxVar.grid(row=0, column=0)

#Scatter Frame column 0
#====================================================================



#====================================================================
#=========================Interval Plot Frame========================
#====================================================================

        self.intervalLabel = Label(self.intervalFrame, text="Interval Plot Label")
        self.intervalLabel.grid(row=0,column=0)

#function to show options for selected graph type
#====================================================================
    def graphOptionSelected(self, selected):

        if selected == "Scatterplot":
            self.intervalFrame.grid_remove()
            self.scatterFrame.grid(row=2, column=0, padx=3, pady=3)
        elif selected == "Interval Plot":
            self.scatterFrame.grid_remove()
            self.intervalFrame.grid(row=2, column=0, padx=3, pady=3)
        else:
            self.intervalFrame.grid_remove()
            self.scatterFrame.grid_remove()


#function to prompt file selection dialogue
#====================================================================
    def loadFile(self):
        print("will prompt file dialogue")




root = Tk()
main = mainWindow(root)
root.mainloop()