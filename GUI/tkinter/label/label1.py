from tkinter import StringVar, Entry
from tkinter import *

root=Tk(className="123")
root.geometry("500x200")
text="123"
path = StringVar()
path.set(text)
L1 =Label(root, textvariable=path, width=8)
L1.grid(row=0, column=0)
print(dir(Label))
Label.bind()

root.mainloop()