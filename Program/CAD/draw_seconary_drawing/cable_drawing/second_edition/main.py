from tkinter import *
from tkinter.filedialog import askopenfilenames

import xlrd
from pyautocad import APoint, Autocad

"""
拿到excel文件的路径，读取excel文件
提取相关的数据，形成字典，返回字典供下一步使用
"""
class excel_reader():
    def __init__(self,filelists):
        self.filelists=filelists
        self.result=dict()
        if len(filelists)==1:
            self.filelist=self.filelists[0]
            self.extract_data()
        else:
            print("多个文件暂时无法处理")
    def extract_data(self):
        #处理excel数据
        filelist=self.filelist
        data=xlrd.open_workbook(filelist)
        table=data.sheet_by_index(0)
        col1=table.col_values(3,start_rowx=2)
        col2=table.col_values(4,start_rowx=2)
        col3=table.col_values(7,start_rowx=2)
        col4=table.col_values(8,start_rowx=2)
        self.result["source"]=col1
        self.result["place from"]=col2
        self.result["destination"]=col3
        self.result["place to"]=col4
"""
信号柜的模型
长100，宽15，字体高度4
"""
class cabinet():
    def __init__(self,name=None):
        chang = 100
        kuan = 15
        wenzi_height = 4
        AlignNum = 4
        self.point1 = APoint(0, 0)
        self.point2 = APoint(chang, 0)
        self.point3 = APoint(chang, kuan)
        self.point4 = APoint(0, kuan)
        self.wenzi_insert_point = APoint(chang / 2, kuan / 2)
        self.wenzi_height = wenzi_height
        self.wenzi_alignNum = AlignNum
        self.name=name

    @property
    def draw_info(self):
        line1 = [self.point1, self.point2]
        line2 = [self.point2, self.point3]
        line3 = [self.point3, self.point4]
        line4 = [self.point4, self.point1]
        line_info = [line1, line2, line3, line4]
        wenzi_info = [self.name, self.wenzi_insert_point, self.wenzi_height, self.wenzi_alignNum]
        arc_info = []
        info = [line_info, wenzi_info, arc_info]
        return info
"""
端子排的模型
长25，宽15，字体高度4
"""
class BN():
    def __init__(self,name):
        chang = 25
        kuan = 15
        wenzi_height = 4
        AlignNum = 4
        self.point1 = APoint(0, 0)
        self.point2 = APoint(chang, 0)
        self.point3 = APoint(chang, kuan)
        self.point4 = APoint(0, kuan)
        self.wenzi_insert_point = APoint(chang / 2, kuan / 2)
        self.wenzi_height = wenzi_height
        self.wenzi_alignNum = AlignNum
        self.name = name

    @property
    def draw_info(self):
        line1 = [self.point1, self.point2]
        line2 = [self.point2, self.point3]
        line3 = [self.point3, self.point4]
        line4 = [self.point4, self.point1]
        line_info = [line1, line2, line3, line4]
        wenzi_info = [self.name, self.wenzi_insert_point, self.wenzi_height, self.wenzi_alignNum]
        arc_info = []
        info = [line_info, wenzi_info, arc_info]
        return info


"""
总的CAD画图控制器
1、通过excel_reader类，完成对excel文件的处理，数据提取
2、建立信号模型，柜子模型等制图基本单元
3、布置相关基本块，成图
"""
class CADdrawer():
    def __init__(self,filelist):
        self.filelist=filelist[0]
        #处理输入的文件路径
        filelists=self.process_filelist()
        #处理excel
        excel_rd=excel_reader(filelists)
        # 返回处理excel的结果
        result=excel_rd.result
        #准备块的信息
        self.blocklistinfo=[]
        #准备块的布置信息
        self.place_info=[]
        #画块
        self.draw_cad_model(result)
        print(self.blocklistinfo)
        #布置块
        self.place_kuai(self.blocklistinfo)
        #画电缆
        self.draw_cable()
        #写电缆编号
        self.draw_cable_name()
    #处理文件路径
    def process_filelist(self):
        filelists=[]
        for i in self.filelist:
            filelists.append(i)
        return filelists
    #画直线
    def draw_line(self,blockObj, line_info):
        if line_info == []:
            pass
        else:
            for l_info in line_info:
                point1 = l_info[0]
                point2 = l_info[1]
                blockObj.AddLine(point1, point2)
    #画文字
    def draw_wenzi(self,blockObj, wenzi_info):
        if wenzi_info == []:
            pass
        else:
            textObj = blockObj.AddText(wenzi_info[0], wenzi_info[1], wenzi_info[2])
            AlignNum = wenzi_info[3]
            textObj.Alignment = AlignNum
            insertPnt = wenzi_info[1]
            textObj.TextAlignmentPoint = insertPnt
    #画cabinet块
    def draw_cabinet_model(self,info):
        draw_info=info
        for i in draw_info:
            c=cabinet(name=i)
            model_info = c.draw_info
            line_info = model_info[0]
            wenzi_info = model_info[1]
            arc_info = model_info[2]
            block_start_point = APoint(0, 0)
            blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
            self.draw_line(blockObj, line_info)
            self.draw_wenzi(blockObj, wenzi_info)
            self.blocklistinfo.append(wenzi_info[0])
    #画BN块
    def draw_BN_model(self,info):
        BN_info = info
        for item in BN_info:
            c = BN(item)
            model_info = c.draw_info
            line_info = model_info[0]
            wenzi_info = model_info[1]
            arc_info = model_info[2]
            block_start_point = APoint(0, 0)
            blockObj = acad.ActiveDocument.Blocks.Add(block_start_point, wenzi_info[0])
            self.draw_line(blockObj, line_info)
            self.draw_wenzi(blockObj, wenzi_info)
            self.blocklistinfo.append(wenzi_info[0])
    #依据返回的excel处理的result结果，开始画块
    def draw_cad_model(self,result=None):
        from_cabinet_info=result["source"]
        to_cabinet_info=result["destination"]
        from_BN_info=result["place from"]
        to_BN_info=result["place to"]
        #画cabinet块
        self.draw_cabinet_model(from_cabinet_info)
        # 画BN块
        self.draw_BN_model(from_BN_info)
        # 画BN块
        self.draw_BN_model(to_BN_info)
        # 画cabinet块
        self.draw_cabinet_model(to_cabinet_info)
    #具体每一列的布置块
    def place_cabinet(self,place_info, block_info):
        for insertionPnt, load_name in zip(place_info, block_info):
            acad.model.InsertBlock(insertionPnt, load_name, 1, 1, 1, 0)
    def place_kuai(self,blockinfo):
        for i in range(33):
            self.place_info.append(APoint(0, i * 15))
        for i in range(33):
            self.place_info.append(APoint(100,i*15))
        for i in range(33):
            self.place_info.append(APoint(225, i * 15))
        for i in range(33):
            self.place_info.append(APoint(250,i*15))
        self.place_cabinet(self.place_info, blockinfo)
        print(self.place_info,blockinfo)
    #画电缆
    def draw_cable(self):
        for i in range(33):
            p1=APoint(125,7.5+i*15)
            p2=APoint(225,7.5+i*15)
            acad.model.AddLine(p1, p2)
    #写电缆编号
    def draw_cable_name(self):
        for i in range(33):
            p1=APoint(150,8+i*15)
            acad.model.AddText('电缆 %s' % (i+1), p1, 5)
"""
创立一个新frame
创建输出CAD文件frame
第一行，label 请确认CAD软件已打开
第二行，按钮，在桌面生成CAD文件
"""
class result_frame(Frame):
    def __init__(self,root=None,filelist=None):
        super().__init__(root)
        self.filelist = filelist
        L1 = Label(self, text="请确认CAD软件已打开")
        B1 = Button(self, text="生成CAD文件", command=lambda: self.draw(self.filelist), height=1)
        L1.pack(pady=10)
        B1.pack()

    def draw(self, filelsit):
        filelsit = filelsit
        CADdrawer(filelsit)
"""
建立自定义的Frame
创建输入文件信号frame
第一行，有输入文件label，文件框，选择文件按钮   选择文件后，所选文件路径会赋值到自身frame的参数中
第二行，一个生成CAD文件的按钮，产生一个新的窗口，并将自身frame收集到的文件路径作为参数，传到新的窗口
"""
class input_file_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filelist = []
        L1 = Label(self, text="输入文件:")
        L1.grid(row=0, column=0)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=0, column=2, padx=3)
        B2 = Button(self, text="完成文件输入", command=lambda: self.checkInput(), height=1)
        B2.grid(row=0, column=3, padx=3)
        B3 = Button(self, text="生成CAD文件", command=lambda: self.createNewWindow(self.filelist), height=1)
        B3.grid(row=1, column=1, padx=3)

    def selectPath(self, path1):
        path_ = askopenfilenames()
        path1.set(path_)
        self.filelist = []
        self.filelist.append(path_)

    def checkInput(self):
        L2 = Label(self, text="√")
        L2.grid(row=0, column=4, padx=3)

    def createNewWindow(self, filelist):
        root1 = Tk(className="CAD文件生成")
        root1.geometry("200x100")
        if filelist == []:
            L1 = Label(root1, text="请输入文件路径")
            L1.pack(pady=10)
        else:
            r_frame = result_frame(root1, filelist)
            r_frame.pack()
        root1.mainloop()

#建立初始窗口类
class basic_window(Tk):
    def __init__(self):
        super().__init__(className="二次图制作")
        ipf_frame=input_file_frame(self)
        ipf_frame.pack()
        self.geometry("500x100")

if __name__=="__main__":
    acad = Autocad(create_if_not_exists=True)
    root=basic_window()
    root.mainloop()