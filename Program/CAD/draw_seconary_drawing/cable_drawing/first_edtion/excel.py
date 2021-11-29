import xlrd

class read_excel():
    def __init__(self,filelist):
        self.file=filelist
        self.result=dict()
        if type(self.file) is str:
            self.extract_data()
        else:
            print("输入多个文件，暂时不处理")

    def extract_data(self):
        #处理excel数据
        filelist=self.file
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

#试验用时
# rd_excel=read_excel("C:\\Users\\zlt\\Desktop\\GPA_电缆.xls")
