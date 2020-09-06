from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont

class input_root(Tk):
    def __init__(self):
        super().__init__(className="仪表逻辑图")
        super().geometry("900x400")