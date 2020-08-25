from tkinter import *
from tkinter import ttk

root=Tk(className="仪表逻辑图")
root.geometry("600x200")
f1=Frame(root,height = 20,width = 400)
b1=Button(f1,text="13")
b1.grid()
f1.pack()
for i in dir(f1):
    print(i)
print("_________________________")
for k,v in f1.__dict__.items():
    print(str(k)+":"+str(v))
root.mainloop()