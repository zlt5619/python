import tkinter as tk
root = tk.Tk()
from tkinter.filedialog import askopenfilename

def printfilepath():
    path=askopenfilename()
    print(path)

B=tk.Button(root,text="选择文件",command=printfilepath())
B.pack()
root.mainloop()