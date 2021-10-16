from tkinter import *
from tkinter.filedialog import askopenfilenames

from pyautocad import Autocad, APoint
import xlrd
#定制输入文件框
class input_Frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filelist = []
        self.text_list=dict()
        L1 = Label(self, text="输入文件:")
        L1.grid(row=1, column=0)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=1, column=1)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(self.path1), height=1)
        B1.grid(row=1, column=2, padx=3)
        B2 = Button(self, text="完成文件输入", command=lambda: self.checkInput(), height=1)
        B2.grid(row=1, column=3, padx=3)
        B3 = Button(self, text="画表格", command=lambda: self.draw_cad(), height=1)
        B3.grid(row=2, column=1, padx=3)

    def selectPath(self, path1):
        path_ = askopenfilenames()
        path1.set(path_)
        self.filelist = []
        self.filelist.append(path_)

    def checkInput(self):
        L2 = Label(self, text="√")
        L2.grid(row=1, column=4, padx=3)

    def draw_cad(self):
        draw_info = self.read_excel()
        acad = Autocad(create_if_not_exists=True)
        acad.ActiveDocument.ActiveTextStyle.SetFont("楷体", False, False, 1, 0 or 0)
        x_wenzi = [0]
        x_line = [0]
        for i in range(len(draw_info)):
            # 先确定横坐标
            width = draw_info[i][-1]
            zuobiao_x = x_wenzi[i] + width * 4
            x_wenzi.append(zuobiao_x)
            if i == 0:
                x_line[0] = x_line[0] - width * 2
            x_line.append(zuobiao_x - width * 2)
        zongchang = x_wenzi.pop(-1)
        for i in range(len(draw_info)):
            content = draw_info[i][:-1]
            for j in range(len(content)):
                p1 = APoint(x_wenzi[i], 0 - j * 5)
                textObj = acad.model.addText(str(content[j]), p1, 2.5)
                AlignNum = 4
                textObj.Alignment = AlignNum
                textObj.TextAlignmentPoint = p1
        col = len(draw_info)
        row = len(draw_info[0])
        for i in range(col):
            p1 = APoint(x_line[i], 2.5)
            p2 = APoint(x_line[i], 2.5 - (row - 1) * 5)
            acad.model.addLine(p1, p2)
        p1 = APoint(x_line[-1] + 5, 2.5)
        p2 = APoint(x_line[-1] + 5, 2.5 - (row - 1) * 5)
        acad.model.addLine(p1, p2)
        for i in range(row):
            p1 = APoint(-10, 2.5 - i * 5)
            p2 = APoint(-10 + zongchang + 11, 2.5 - i * 5)
            acad.model.addLine(p1, p2)

    def read_excel(self):
        draw_info=[]
        file=self.filelist[0][0]
        wb = xlrd.open_workbook(file)
        sheet1 = wb.sheet_by_index(0)
        for r in range(sheet1.ncols):
            draw_info.append(sheet1.col_values(r))
        for i in draw_info:
            i.pop(0)
            i.pop(1)
            max=0
            for j in i:
                if len(str(j))>max:
                    max=len(str(j))
            i.append(max)
        return draw_info


if __name__=="__main__":
    root=Tk(className="画excel表格")
    root.geometry("430x100")
    ipf=input_Frame(root)
    ipf.pack()
    root.mainloop()