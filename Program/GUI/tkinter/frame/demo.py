from tkinter import *
from tkinter import ttk

root=Tk(className="仪表逻辑图")
root.geometry("600x200")
f1=Frame(height = 20,width = 400)
b1=Button(f1,text="13")
b1.grid()
f1.pack()
print(b1.grid_info()["row"])
root.mainloop()