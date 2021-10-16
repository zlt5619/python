from tkinter import *

import xlrd

"""
处理frame
一般有多个按钮，按钮指向不同的功能
这个最基础的功能，就是读取excel全部内容
需要传递两个参数，root和filelists，root为该frame所在的地方，filelists是这个frame的文件清单输入
"""


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


class process_excel_frame(Frame):
    def __init__(self,root=None,filelists=[]):
        super().__init__(root)
        #接受上一级传递过来的文件清单
        self.filelists=filelists
        self.excel_processor=Excel_Processor(self.filelists)
        self.data1=None
        self.data2=None
        B1=Button(self, text="处理？？？", command=lambda: self.process(), height=1)
        B1.pack()
    #提取excel相关数据
    def process(self):
        self.data1=self.excel_processor.excel_row_data
        self.data2=self.excel_processor.excel_col_data

