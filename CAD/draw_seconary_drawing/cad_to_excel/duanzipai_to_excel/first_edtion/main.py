from tkinter import Tk, Frame, Button, Label, Entry, StringVar
from tkinter.filedialog import askopenfilenames

from pyautocad import Autocad
import xlwt

def function1():



    all_info=[]


    for obj in acad.iter_objects("Text"):
        a=obj.TextString
        b=obj.InsertionPoint
        l=[a,b]
        all_info.append(l)

    # print(all_info)
    #找到端子排
    max=0
    duanzipai=None
    value=None
    for i in all_info:
        if i[1][1]>=max:
            max=i[1][1]
            duanzipai=i[0]
            value=i[1]
    # print(duanzipai)
    #删除端子排
    all_info.remove([duanzipai,value])
    # print(all_info)

    #找到左侧端子排
    zuoce=[]
    for i in all_info:
        if i[1][0]>27 and i[1][0]<47:
            zuoce.append([i[0],i[1]])
    # print(zuoce)

    #找到中间端子排
    zhongjian=[]
    for i in all_info:
        if i[1][0]>47 and i[1][0]<57:
            zhongjian.append([i[0],i[1]])
    # print(zhongjian)

    #找到右侧端子排
    youce=[]
    for i in all_info:
        if i[1][0]>57 and i[1][0]<77:
            youce.append([i[0],i[1]])
    # print(youce)

    #找到右侧文字注释
    wenzi=[]
    for i in all_info:
        if i[1][0]>77:
            wenzi.append([i[0],i[1]])
    # print(wenzi)

    jieguo=[]
    for i in zhongjian:
        result=[]
        result.append(i[0])
        y=i[1][1]
        flag=0
        for j in zuoce:
            if j[1][1]>y-2 and j[1][1]<y+2:
                result.append(j[0])
                flag=1
        if flag==1:
            flag=0
        else:
            result.append(" ")
        for j in youce:
            if j[1][1] > y - 2 and j[1][1] < y + 2:
                result.append(j[0])
                flag = 1
        if flag == 1:
            flag = 0
        else:
            result.append(" ")
        for j in wenzi:
            if j[1][1] > y - 2 and j[1][1] < y + 2:
                result.append(j[0])
                flag = 1
        if flag == 1:
            flag=0
        else:
            result.append(" ")
        jieguo.append(result)
    """
    ['1', 'A01', ' ', ' ']
    ['9', 'A1003', '101URXXXX', '500kV系统联跳']
    ['12', 'A1009', '101URXXXX', '柜B跳闸起动GCB失灵开入']
    ['10', 'A1005', '101URXXXX', 'GCB跳闸位置']
    ['11', 'A1007', '101URXXXX', '主汽门位置接点']
    ['6', ' ', ' ', ' ']
    ['8', 'A1001', '101URXXXX', '汽机保护系统动作']
    ['7', ' ', ' ', ' ']
    ['5', 'A01', '411BN-23', ' ']
    ['4', 'A01', ' ', ' ']
    ['3', 'A01', ' ', ' ']
    ['2', 'A01', ' ', ' ']
    ['13', ' ', ' ', ' ']
    ['14', ' ', ' ', ' ']
    ['15', ' ', ' ', ' ']
    """
    # for i in jieguo:
    #     print(i)

    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    worksheet.write(0,0, label = '端子排')
    worksheet.write(1,0, label = duanzipai)
    worksheet.write(0,1, label = '端子排号')
    worksheet.write(0,2, label = '左侧端子排')
    worksheet.write(0,3, label = '右侧端子排')
    worksheet.write(0,4, label = '右侧输出')
    # 参数对应 行, 列, 值
    for i in range(15):
        worksheet.write(int(jieguo[i][0]),1,label=jieguo[i][0])
        worksheet.write(int(jieguo[i][0]),2,label=jieguo[i][1])
        worksheet.write(int(jieguo[i][0]),3,label=jieguo[i][2])
        worksheet.write(int(jieguo[i][0]),4,label=jieguo[i][3])


    workbook.save('Excel_test.xls')

"""
输入环节
第一行 按钮，将cad文件形成excel文件
第二行 输入文件路径，比较文件，根据新文件生成新的cad
"""
class input_Frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filelist = []
        b1=Button(self, text="生成excel", command=function1(), height=1)
        b1.grid(row=0, column=1)
        L1 = Label(self, text="输入文件:")
        L1.grid(row=1, column=0)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=1, column=1)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=1, column=2, padx=3)
        B2 = Button(self, text="完成文件输入", command=lambda: self.checkInput(), height=1)
        B2.grid(row=1, column=3, padx=3)
        B3 = Button(self, text="修改CAD文件", command=lambda: self.redraw(self.filelist), height=1)
        B3.grid(row=2, column=1, padx=3)

    def selectPath(self, path1):
        path_ = askopenfilenames()
        path1.set(path_)
        self.filelist = []
        self.filelist.append(path_)

    def checkInput(self):
        L2 = Label(self, text="√")
        L2.grid(row=0, column=4, padx=3)

    def redraw(self,filelist):
        acad.iter_objects("Text")

if __name__=="__main__":
    acad = Autocad(create_if_not_exists=True)
    root=Tk(className="二次图需求")
    root.geometry("500x200")
    in_frame=input_Frame(root)
    in_frame.pack()
    root.mainloop()