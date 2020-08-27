from tkinter import StringVar, Entry
from tkinter import *

root=Tk(className="123")
root.geometry("500x200")

for i in range(10):
    text=str(i)
    path=StringVar()
    path.set(text)
    E1 = Entry(root, textvariable=path, width=8)
    E1.grid(row=i, column=0)


print(dir(Entry))

root.mainloop()