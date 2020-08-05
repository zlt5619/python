import tkinter as tk
root = tk.Tk()
from tkinter.filedialog import askopenfilename,askopenfilenames,askdirectory,asksaveasfilename

#这个对话框，可以让用户选择一个文件,选择一个文件，返回此文件路径的字符串，如果不选择，Cancel或直接关闭，返回一个空的字符串
path=askopenfilename()
print(path)


