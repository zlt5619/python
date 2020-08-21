from tkinter import *
from tkinter import ttk

root=Tk(className="仪表逻辑图")
root.geometry("600x200")
f2=Frame(root)
#以不同的颜色区别各个frame
# for fm in ['red','blue','yellow','green','white','black']:
#     #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
#     Frame(height = 20,width = 400,bg = fm).pack()


#以不同的颜色区别各个frame
# for color in ['red','blue']:
#     #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
#     fm.append(Frame(height = 200,width = 400,bg = color))
# #向下面的Frame中添加一个Label
# Label(fm[1],text = 'Hello label').pack()
# fm[0].pack()
# fm[1].pack()
# f1=Frame(height = 100,width = 400,bg="red")
# f2=Frame(height = 100,width = 400,bg="blue")
# Button(f1,text = 'Hi label').pack()
# Button(f2,text = 'Hello label').pack()
# f1.pack()
# f2.pack()
# def addBox():
#     e1 = ttk.Combobox(f1, width=3)
#     e1.pack(side=LEFT, padx=5)
#     e2 = Entry(f1, width=7)
#     e2.pack(side=LEFT, padx=5)
# f1=Frame(height = 20,width = 400)
# L1 = Label(f1,text="123", width=5)
# L1.pack(side=LEFT)
# L2 = Label(f1, text="=", width=3)
# L2.pack(side=LEFT)
# E2 = Entry(f1, width=7)
# E2.pack(side=LEFT,padx=5)
# E3 = ttk.Combobox(f1, width=3)
# E3.pack(side=LEFT,padx=5)
# E4 = Entry(f1, width=7)
# E4.pack(side=LEFT,padx=5)
# B5 = Button(f1, text="完成")
# B5.pack(side=RIGHT)
# B4 = Button(f1, text="+",command=lambda :addBox())
# B4.pack(side=RIGHT,padx=5)
# f1.pack()

#增加输入框
def addBox(frame,button1,button2,button3):
    row=button1.grid_info()['row']
    column=button1.grid_info()['column']
    e1 = ttk.Combobox(f1,value=str1, width=3)
    e1.grid(row=row,column=column)
    e2 = Entry(f1, width=7)
    e2.grid(row=row,column=column+1)
    button1.grid(row=row,column=column+2)
    button2.grid(row=row, column=column+3)
    button3.grid(row=row, column=column+4)
    frame.element[row].append(e1)
    frame.element[row].append(e2)

#减少输入框
def subBox(frame,button1,button2,button3):
    row = button1.grid_info()['row']
    column = button1.grid_info()['column']
    obj1=frame.element[row].pop()
    obj2=frame.element[row].pop()
    obj1.destroy()
    obj2.destroy()
    button1.grid(row=row, column=column -2)
    button2.grid(row=row, column=column -1)
    button3.grid(row=row, column=column)

#再画一行
def draw_another_row(frame,buttom3):
    input_list=[]
    row=frame.row[-1]
    current_row=buttom3.grid_info()['row']
    column=buttom3.grid_info()['column']
    L1 = Label(f1, text="√", width=3)
    L1.grid(row=row, column=column + 1)
    for i in range(len(frame.element[current_row])):
        if i==0:
            pass
        else:
            input_list.append(frame.element[row][i].get())
    print(input_list)
    print(current_row)
    print(row)
    for i in range(len(input_list)):
        if "信号" in input_list[i] :
            row+=1
            frame.row.append(row)
            print(frame.row)
            draw_basic_function(frame,text=input_list[i])
#画基本的一行
def draw_basic_function(frame,text="输出信号"):
    f1=frame
    row=f1.row[-1]
    path=StringVar()
    path.set(text)
    E1 = Entry(f1, text=path, width=8)
    E1.grid(row=row, column=0)
    L2 = Label(f1, text="=", width=3)
    L2.grid(row=row, column=1)
    E2 = Entry(f1, width=7)
    E2.grid(row=row, column=2)
    E3 = ttk.Combobox(f1, value=str1, width=3)
    E3.grid(row=row, column=3, padx=3)
    E4 = Entry(f1, width=7)
    E4.grid(row=row, column=4, padx=3)
    B1 = Button(f1, text="+", command=lambda: addBox(f1, B1, B2, B3))
    B1.grid(row=row, column=5, padx=3)
    B2 = Button(f1, text="-", command=lambda: subBox(f1, B1, B2, B3))
    B2.grid(row=row, column=6, padx=3)
    B3 = Button(f1, text="完成", command=lambda: draw_another_row(f1,B3))
    B3.grid(row=row, column=7, padx=3)
    f1.element[row] = [ E1, E2, E3,E4]

#汇总所有输入信号
def get_all_info(frame):
    row=frame.row[-1]
    print_info=[]
    for i in range(row+1):
        print_info.append(frame.element[i])
    for i in print_info:
        for j in i:
            print(j.get())

#在f2框架内，加入f1输入框架和b输出总按钮
f1=Frame(f2,height = 20,width = 400)
f1.row=[0]
f1.column=[7]
f1.element=dict()
str1=["&&","||"]
f1.element[0]=[]
draw_basic_function(f1)
f1.grid(row=0,sticky=W)
b=Button(f2,text="完成编写",command=lambda :get_all_info(f1))
b.grid(row=1)
f2.pack()
root.mainloop()