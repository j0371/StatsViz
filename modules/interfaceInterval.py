import tkinter as tk
from tkinter import ttk

class IntervalFrame:

    def __init__(self, frame):

        self.intervalLabel = tk.Label(frame, text="Interval Plot Label")
        self.intervalLabel.grid(row=0,column=0)