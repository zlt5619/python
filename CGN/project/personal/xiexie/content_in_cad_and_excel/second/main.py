from tkinter import *
from tkinter.filedialog import askopenfilenames

import xlrd
import xlwt


from pyautocad import Autocad
class Row_Writer():
    def __init__(self,data=None,filepath=None,filename="data.xls"):
        self.data=data
        if filepath==None:
            self.filepath= "../"
        else:
            self.filepath=filepath
        self.filename=filename
        self.write_excel()
    #制作相关文件夹
    def write_excel(self):
        book = xlwt.Workbook()
        sheet1=book.add_sheet(sheetname="例子1")
        for i in range(len(self.data)):
            row_content=self.data[i+1]
            for j in range(len(row_content)):
                sheet1.write(i,j,row_content[j])
        filepath_name=self.filepath+self.filename
        book.save(filepath_name)

#excel模块
class Excel_Processor():
    def __init__(self,filelists=[]):
        self.filelists=filelists
        self.excel_row_data=dict()
        self.sheets_row_data=dict()
        self.excel_col_data=dict()
        self.sheets_col_data=dict()
        if len(self.filelists)==1:
            self.process_single_excel(self.filelists[0])
        else:
            self.process_multiple_excels()

    #处理单个文件
    def process_single_excel(self,file):
        self.sheets_row_data =dict()
        file=file
        #处理得到文件名
        if "\\" in file:
            temp1=file.split("\\")
            temp2=temp1[-1].split(".")
            filename=temp2[0]
        else:
            temp1 = file.split("/")
            temp2 = temp1[-1].split(".")
            filename = temp2[0]
        #读取excel表
        excel = xlrd.open_workbook(file)
        sheet_names=excel.sheet_names()
        for i in range(len(sheet_names)):
            sheet=excel.sheet_by_name(sheet_names[i])
            sheet_rows=sheet.nrows
            sheet_cols=sheet.ncols
            sheet_row_data=dict()
            sheet_col_data=dict()
            #按行来读
            for j in range(sheet_rows):
                sheet_row_data[j+1]=sheet.row_values(j)
            self.sheets_row_data[sheet_names[i]]=sheet_row_data
            #按列来读取
            for j in range(sheet_cols):
                sheet_col_data[j+1]=sheet.col_values(j)
            self.sheets_col_data[sheet_names[i]]=sheet_col_data
        self.excel_row_data[filename]=self.sheets_row_data
        self.excel_col_data[filename]=self.sheets_col_data
    #处理多个文件转为循环处理单个文件
    def process_multiple_excels(self):
        for i in self.filelists:
            self.process_single_excel(i)

def readexcel(filelists):
    data = dict()
    ep = Excel_Processor(filelists)
    excel = ep.excel_row_data
    data = excel['新建 Microsoft Excel 工作表']["Sheet1"]
    return data
#读取cad文件，生成设备名称和设备房间
#格式为{1，[设备名，房间号]，2：[设备名，房间号]}
def readcad():
    data=dict()
    acad = Autocad(create_if_not_exists=True)
    equipment_info=[]
    rest_info=[]
    for obj in acad.iter_objects("Text"):
        obj_x=obj.InsertionPoint[0]
        obj_y=obj.InsertionPoint[1]
        obj_text=obj.TextString
        list1=[obj_text,obj_x,obj_y]
        if len(obj_text)==4 and obj_text.startswith("2"):
            equipment_info.append(list1)
        else:
            #通过旋转角度判断是否入选
            if obj.Rotation==0:
                rest_info.append(list1)
    for i in range(len(equipment_info)):
        for j in rest_info:
            if equipment_info[i][2]-0.5 < j[2] < equipment_info[i][2]+0.5:
                if equipment_info[i][1]<j[1]<equipment_info[i][1]+15:
                    string1=equipment_info[i][0]+j[0]
                    data[i+1]=string1
    for i in range(len(equipment_info)):
        for j in rest_info:
            if equipment_info[i][2]-10 < j[2] < equipment_info[i][2]:
                if equipment_info[i][1]-3<j[1]<equipment_info[i][1]+2:
                    string2=j[0]
                    string1=data[i+1]
                    list1=[string1,string2]
                    data[i+1]=list1
    return data
#直接在原excel里增加cad读取的信息
def excelcreate(filelists):
    excel_data=readexcel(filelists)
    cad_data=readcad()
    filepath = str()
    temp = filelists[0].split("/")
    temp1 = temp[:-1]
    filaname=temp[-1]+"1"
    for i in temp1:
        filepath = filepath + i + "/"
    for k1,v1 in excel_data.items():
        for k2,v2 in cad_data.items():
            if v2[0] in v1[0]:
                v1.append(v2[0])
                v1.append(v2[1])
                excel_data[k1]=v1
    rw=Row_Writer(data=excel_data,filepath=filepath,filename=filaname)



#定义修改cad功能
def cadchange(filelists):
    print(filelists)
#输入路径模块
class input_filepath_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.filelists=[]
        self.actual_path=None
        #用于在文本框显示已选择的文件
        self.text_path = StringVar()
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0)
        E1 = Entry(self, textvariable=self.text_path, width=30)
        E1.grid(row=0, column=1)
        B1 = Button(self, text="...", command=lambda: self.selectPath(), height=1)
        B1.grid(row=0, column=2, padx=3)

    def selectPath(self):
        self.text_path.set(" ")
        self.filelists = []
        self.actual_path=askopenfilenames()
        self.text_path.set(self.actual_path)
        for i in self.actual_path:
            self.filelists.append(i)
"""
整体模块
1、输入路径
2、输出excel
3、比较cad
"""
class MainFrame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        ipf=input_filepath_frame(self)
        ipf.grid(row=0, column=0,padx=50,pady=10)
        B1=Button(self,text="生成excel文件",command=lambda: self.createnewexcel(ipf.filelists), height=1)
        B1.grid(row=1, column=0,pady=10)
        B2=Button(self,text="修改cad文件",command=lambda: self.changecad(ipf.filelists), height=1)
        B2.grid(row=2, column=0,pady=10)
    #生成新的excel文件
    #跳出弹窗，提示确认cad已打开，再加上按键
    def createnewexcel(self,filelists):
        root1=Tk(className="提示")
        root1.geometry("200x150")
        L1=Label(root1, text="请确认cad文件已打开")
        L1.pack(pady=20)
        B3=Button(root1,text="生成excel",command=lambda:excelcreate(filelists), height=1)
        B3.pack(pady=10)
        root1.mainloop()
    #修改原来的cad文件
    # 跳出弹窗，提示确认cad已打开，再加上按键
    def changecad(self,filelists):
        root1 = Tk(className="提示")
        root1.geometry("200x150")
        L1 = Label(root1, text="请确认cad文件已打开")
        L1.pack(pady=20)
        B4 = Button(root1, text="修改cad", command=lambda:cadchange(filelists), height=1)
        B4.pack(pady=10)
        root1.mainloop()

#主程序
if __name__=="__main__":
    root=Tk(className="比较器")
    root.geometry("400x200")
    mainframe=MainFrame(root)
    mainframe.pack()
    root.mainloop()
str