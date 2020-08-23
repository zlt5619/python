from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont
import xlrd
from xlwt import *

root=Tk(className="仪表逻辑图")
root.geometry("900x400")

input_frame=Frame(root,height = 100,width = 800)
button_frame=Frame(root,height = 200,width = 800)
shuchu_frame=Frame(root,height = 50,width = 800)

path1=StringVar()
filelist=[]
input_signal=[]
output_signal=[]
str1=["&&","||"]
data=dict()
Button_dict = dict()
"""
根据所有的信息，绘制excel表格，输出到当前路径
"""
def create_excel(input_signal,output_signal,data):
    ws = Workbook(encoding='utf-8')
    w_input=ws.add_sheet(sheetname="输入信号")
    w_output=ws.add_sheet(sheetname="输出信号")
    if len(data)==0:
        pass
    else:
        #将填写好的输入数据填入Excel中
        pass
    for i in range(len(input_signal)):
        w_input.write(i,0,input_signal[i])
    for j in range(len(output_signal)):
        w_output.write(j,0,output_signal[j])
    ws.save("输出文件.xls")

fontStyle1 = tkFont.Font(size=20)
B3=Button(shuchu_frame,font=fontStyle1,text="输出形成excel表格",command=lambda :create_excel(input_signal,output_signal,data))
B3.grid(row=0,column=0)

"""
根据不同的按钮，跳到输出界面
"""
#增加输入框
def addBox(frame,button1,button2,button3):
    row=button1.grid_info()['row']
    column=button1.grid_info()['column']
    e1 = ttk.Combobox(frame,value=str1, width=3)
    e1.grid(row=row,column=column)
    e2 = Entry(frame, width=7)
    e2.grid(row=row,column=column+1)
    button1.grid(row=row,column=column+2)
    button2.grid(row=row, column=column+3)
    button3.grid(row=row, column=column+4)

#减少输入框
def subBox(frame,button1,button2,button3):
    row = button1.grid_info()['row']
    column = button1.grid_info()['column']
    if len(frame.grid_slaves())==8:
        pass
    else:
        obj1=frame.grid_slaves().pop(0)
        obj1.destroy()
        obj2=frame.grid_slaves().pop(0)
        obj2.destroy()
        button1.grid(row=row, column=column -2)
        button2.grid(row=row, column=column -1)
        button3.grid(row=row, column=column)
#再画一行
def draw_another_row(f_zong,j):
    row = f_zong.grid_size()[1]
    f = Frame(f_zong, height=20, width=400)
    f.grid(row=row, sticky=W)

    draw_basic_row(f,str1,text=j,f_zong=f_zong)

def collect_info_and_draw_another_row(frame,f_zong,buttom3,bd=None):
    info_obj_1=[]
    info_obj_2=[]
    info_obj=[]
    add_list=[]
    index=0
    daichulixinhao=[]
    panduan=0
    L=None
    Button_dict=bd
    if len(frame.grid_slaves())==8:
        info_obj_1=frame.grid_slaves()[-5:]
    else:
        info_obj_1 = frame.grid_slaves()[-5:]
        info_obj_2=frame.grid_slaves()[:-8]
    info_list=[]
    info_obj=info_obj_2+info_obj_1
    info_obj.reverse()
    #收集所有的输入信号
    if len(info_obj)%2==0:
        L=info_obj.pop()
        panduan=1
    for i in range(len(info_obj)):
        if i==0 or i==1:
            info_list.append(info_obj[i].cget("text"))
        else:
            info_list.append(info_obj[i].get())
    #处理输入信号,若输入信号，不在输入输出信号清单，报错，若有中间信号在，生成新的一行，然后打勾
    current_row = buttom3.grid_info()['row']
    column = buttom3.grid_info()['column']
    for j in range(len(info_list)):
        if j==0 or j==1:
            pass
        else:
            if info_list[j] not in input_signal and info_list[j] not in str1:
                daichulixinhao.append(info_list[j])
    for k in daichulixinhao:
        if "信号" in k:
            add_list.append(k)

    if len(add_list)!=len(daichulixinhao):
        L1 = Label(frame, text="输入信号不存在", width=15)
        L1.grid(row=current_row, column=column + 1)
    else:
        if panduan:
            L.destroy()
        L1 = Label(frame, text="√", width=3)
        L1.grid(row=current_row, column=column + 1)
        for i in range(len(f_zong.grid_slaves())):
            if frame == f_zong.grid_slaves()[i]:
                index = len(f_zong.grid_slaves()) - i
        Button_dict[index] = info_list

        for k in add_list:
            draw_another_row(f_zong, k)


def draw_basic_row(frame,str1,text=None,f_zong=None,d=None):
    frame=frame
    row=frame.grid_size()[0]
    b_d=d
    L1 = Label(frame, text=text, width=8)
    L1.grid(row=row, column=0)
    L2 = Label(frame, text="=", width=3)
    L2.grid(row=row, column=1)
    E2 = Entry(frame, width=7)
    E2.grid(row=row, column=2)
    E3 = ttk.Combobox(frame, value=str1, width=3)
    E3.grid(row=row, column=3, padx=3)
    E4 = Entry(frame, width=7)
    E4.grid(row=row, column=4, padx=3)
    B1 = Button(frame, text="+", command=lambda: addBox(frame, B1, B2, B3))
    B1.grid(row=row, column=5, padx=3)
    B2 = Button(frame, text="-", command=lambda: subBox(frame, B1, B2, B3))
    B2.grid(row=row, column=6, padx=3)
    B3 = Button(frame, text="完成", command=lambda: collect_info_and_draw_another_row(frame,f_zong,B3,bd=Button_dict))
    B3.grid(row=row, column=7, padx=3)

def get_all_info(output,bd=None):
    Button_dict=bd
    data[output]=Button_dict
    Button_dict=dict()


def jump_to_shuchu(b,data):
    output=b.cget("text")
    root1=Tk(className=output+"的逻辑表达式输入")
    root1.geometry("600x600")
    str1 = ["&&", "||"]

    f_zong = Frame(root1,height=600, width=600)
    # 在f_zong框架内，加入f1输入框架和b输出总按钮,每按一次按钮，增加一个frame，包含1行
    f1 = Frame(f_zong, height=20, width=600)
    f1.grid(row=0, sticky=W)
    f1.content_dict=dict()
    b = Button(root1, text="完成编写", command=lambda: get_all_info(output,bd=Button_dict))

    f_zong.pack()
    b.pack()
    if data==0:
        #当首次没有输入的时候
        draw_basic_row(f1,str1,text=output,f_zong=f_zong,d=Button_dict)

    else:
        #当有参数传递进来的时候
        pass

    root1.mainloop()


"""
根据输入的信号，绘制输入信号按钮，每一行布置6个信号
"""
def draw_button_frame(output_signal,data):

    for i in range(len(output_signal)):
        row=int(i/6)
        column=i%6
        if data:

            b=Button(button_frame,text=output_signal[i],command=lambda : jump_to_shuchu(b,data[output_signal[i]]))
            b.grid(row=row,column=column,padx=10)
        else:
            data = 0
            b = Button(button_frame, text=output_signal[i],
                       command=lambda: jump_to_shuchu(data))
            b.grid(row=row, column=column, padx=10)




"""
在输入部分，分为两部分，
一部分是第一次输入，确定输入信号和输出信号
另一部分是输入已经做好的部分表格
完成输入后，都需要打出完成输入字样
"""


def selectPath(path1):
    path_ = askopenfilename()
    path1.set(path_)
    filelist.append(path_)


def read_file(filelist,data1):
    data=data1
    fontStyle = tkFont.Font(size=20)
    L = Label(input_frame, text="信号输入完成", font=fontStyle)
    L.grid(row=1, column=0)
    workxls = xlrd.open_workbook(filelist[0])
    worksheet_input = workxls.sheet_by_name("输入信号")
    row = worksheet_input.nrows
    for i in range(row):
        rowdata = worksheet_input.row_values(i)[0]  # i行的list
        input_signal.append(rowdata)

    worksheet_output= workxls.sheet_by_name("输出信号")
    row = worksheet_output.nrows
    for i in range(row):
        rowdata = worksheet_output.row_values(i)[0]  # i行的list
        output_signal.append(rowdata)

    # 读取输入文件写好的信号相关内容，并将内容赋给字典data
    excel_list = workxls.sheet_names()[2:]
    if len(excel_list)==0:
        pass
    else:
        for i in excel_list:
            worksheet = workxls.sheet_by_name(i)
            row = worksheet.nrows
            data_list=[]
            for j in range(row):
                rowdata = worksheet.row_values(j)
                data_list.append(rowdata)
            data[i]=data_list
    print("字典为",end=None)
    print(data)
    draw_button_frame(output_signal,data)




L1 = Label(input_frame, text="输入文件:")
L1.grid(row=0,column=0)
E1 = Entry(input_frame, textvariable=path1, width=30)
E1.grid(row=0,column=1)
 # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
B1 = Button(input_frame, text="...", command=lambda :selectPath(path1), height=1)
B1.grid(row=0,column=2,padx=3)
B2 = Button(input_frame, text="完成信号输入", command=lambda :read_file(filelist,data), height=1)
B2.grid(row=0,column=3,padx=3)


input_frame.pack()
button_frame.pack()
shuchu_frame.pack()

root.mainloop()

