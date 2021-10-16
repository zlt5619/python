import xlwt


"""
给定相应的data，形成excel，默认路径为自带文件夹，若要保存至新路径，请给定filepath
data为字典，格式为{1:[...],2:[...],3:[...],...}
"""
class Col_Writer():
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
            col_content=self.data[i+1]
            for j in range(len(col_content)):
                sheet1.write(j,i,col_content[j])
        filepath_name=self.filepath+self.filename
        book.save(filepath_name)



#实例
dt={1:[1,2,3],2:[4,5,6,7,8],3:[9,10,11]}
rw=Col_Writer(data=dt)