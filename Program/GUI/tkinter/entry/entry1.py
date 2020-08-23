from tkinter import StringVar, Entry
from tkinter import *

root=Tk(className="123")
root.geometry("500x200")
text="123"
path = StringVar()
path.set(text)
E1 = Entry(root, textvariable=path, width=8)
E1.grid(row=0, column=0)

root.mainloop()