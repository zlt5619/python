from tkinter import *
from tkinter import ttk
from tkinter import *
root=Tk(className="仪表逻辑图")
root.geometry("350x200")
str1=["s3.5","s7.4","s4.7","s4.6","s4.5","s4.1","s4.10","kus","s3.2"]
str2=["&","|"]
str4=["信号1","信号2","信号3","信号4","信号5","信号6","信号7","信号8","信号9","信号10"]
str3=str1+str4
X=20
Button1_x=0
Button1_y=20
i=[]
path1 = StringVar()
E1=Entry(root, textvariable=path1, width=10)
E1.place(x=X, y=20)
L1=Label(root, text="=")
L1.place(x=X+80,y=20)
C1=ttk.Combobox(root,values=str3,width=5)
C1.place(x=X+100,y=20)
C2=ttk.Combobox(root,values=str2,width=3)
C2.place(x=X+160,y=20)
C3=ttk.Combobox(root,values=str3,width=5)
C3.place(x=X+205,y=20)
def add_combobox(i):
    C1=ttk.Combobox(root,values=str2,width=3)
    C1.place(x=285,y=20)
    C2=ttk.Combobox(root, values=str3, width=5)
    C2.place(x=330,y=20)
    i.append(1)

B1=Button(root,text="+",command=lambda :add_combobox(i))
B1.place(x=285+len(i)*105,y=20)
root.mainloop()


