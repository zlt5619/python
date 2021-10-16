import xlrd
"""
读取相关excel表格，整体读取
可以提供按行读取的数据和按列读取的数据
形式为字典{“excel名1”：{{“sheet名1：{1:"  ",2:"  ",3:"  "}}}，{sheet名2：sheet_data”}}，“excel名2”：{“sheet名1：sheet_data，sheet名2：sheet_data”}，
“excel名3”：{“sheet名1：sheet_data“，”sheet名2：sheet_data”}，。。。}
调用数据时，从[excel表名][sheet名][行/列数]
print(self.excel_row_data)
print(self.excel_row_data["demo"])
print(self.excel_row_data["demo"]["Sheet1"])
print(self.excel_row_data["demo"]["Sheet1"][1])
print(self.excel_col_data)
print(self.excel_col_data["demo - 副本"])
print(self.excel_col_data["demo - 副本"]["Sheet2"])
print(self.excel_col_data["demo - 副本"]["Sheet2"][2])
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
        print(self.excel_row_data)
        # print(self.excel_row_data["demo"])
        # print(self.excel_row_data["demo"]["Sheet1"])
        # print(self.excel_row_data["demo"]["Sheet1"][1])
        print(self.excel_col_data)
        # print(self.excel_col_data["demo - 副本"])
        # print(self.excel_col_data["demo - 副本"]["Sheet2"])
        # print(self.excel_col_data["demo - 副本"]["Sheet2"][2])

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

# e=Excel_Processor(filelists=["D:\\BaiduNetdiskDownload\\二次cad资料\\demo.xlsx"])
# e=Excel_Processor(filelists=["D:\\BaiduNetdiskDownload\\二次cad资料\\demo.xlsx","D:\\BaiduNetdiskDownload\\二次cad资料\\demo - 副本.xlsx"""])
# e=Excel_Processor(filelists=['C:/Users/zlt/Desktop/gengxie/新建 Microsoft Excel 工作表 - 副本.xlsx', 'C:/Users/zlt/Desktop/gengxie/新建 Microsoft Excel 工作表.xlsx'])
e=Excel_Processor(filelists=['C:/Users/zlt/Desktop/gengxie/新建 Microsoft Excel 工作表.xlsx'])