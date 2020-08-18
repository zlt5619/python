from tkinter import ttk
from tkinter import *
root=Tk(className="仪表逻辑图")
root.geometry("600x200")
str1=["s3.5","s7.4","s4.7","s4.6","s4.5","s4.1","s4.10","kus","s3.2"]
str2=["&","|"]
str4=["信号1","信号2","信号3","信号4","信号5","信号6","信号7","信号8","信号9","信号10"]
str3=str1+str4
X=20
Y=50
path1 = StringVar()
path2 = StringVar()
path3 = StringVar()
path4 = StringVar()
E1=Entry(root, textvariable=path1, width=10)
E1.place(x=X, y=Y)
L1=Label(root, text="=",width=5)
L1.place(x=X+80,y=Y)
C1=ttk.Combobox(root,values=str3,width=5,textvariable=path2)
C1.place(x=X+120,y=Y)
C2=ttk.Combobox(root,values=str2,width=3,textvariable=path3)
C2.place(x=X+182,y=Y)
C3=ttk.Combobox(root,values=str3,width=5,textvariable=path4)
C3.place(x=X+230,y=Y)
def addCombobox(Button1,Button2):
    pass
B1=Button(root,text="+",command=lambda :addCombobox(B1,B2))
B1.place(x=X+300,y=Y-5)
B2=Button(root,text="完成")
B2.place(x=X+330,y=Y-5)
root.mainloop()