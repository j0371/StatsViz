import tkinter as tk
from tkinter import ttk

class CommonFrame:

    def __init__(self, frame):

        frame.grid(row=0,column=0, padx=3, pady=3, sticky="EW")

        
        self.graphType = tk.StringVar()
        self.graphType.set("Select Graph Type")

        self.selectedFileVar = tk.StringVar()
        self.selectedFileVar.set("Selected CSV File")


#column 0
#====================================================================
        self.fileButton = tk.Button(frame, text="Select File")
        self.fileButton.grid(row=0, column=0, sticky="W", padx=(10,0), pady=(10,0))

        self.graphOptions = ttk.Combobox(frame, textvariable=self.graphType, values=["Scatterplot", "Interval Plot"], state="readonly")
        self.graphOptions.bind("<<ComboboxSelected>>")
        self.graphOptions.grid(row=2, column=0, columnspan=2, padx=(10,0), pady=5, sticky="W")


#column 1
#====================================================================
        self.selectedFile = tk.Entry(frame, textvariable=self.selectedFileVar, state="readonly", width=39)
        self.selectedFile.grid(row=0, column=1, padx=(3,0), pady=(10,0))

        self.selectedFileScroll = tk.Scrollbar(frame, orient="horizontal", command=self.selectedFile.xview)
        self.selectedFileScroll.grid(row=1,column=1,sticky="ew", pady=(0,10))

        self.selectedFile.config(xscrollcommand=self.selectedFileScroll.set)