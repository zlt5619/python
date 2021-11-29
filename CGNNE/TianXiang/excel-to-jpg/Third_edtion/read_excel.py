import xlrd

path="C:/Users/zlt/Desktop/田祥资料/附件1：中广核新能源控股有限公司2021年08月故障记录汇总表.xlsx"


"""
Excel_file类
添加参数：
path   输入路径

属性

##基本参数
path 文件的路径

##excel的sheet参数
sheet_names excel表格，全部sheet的名称
sheet_num  excel表格，全部sheet的数量


##target_sheet的相关参数       涉及到的方法  get_target_sheet
target_sheet  目标sheet
target_sheet_rows  sheet中总行数
target_sheet_cols  sheet中总列数

#获取target_sheet第一排的具体参数      涉及到的方法  get_first_row_list 输入参数first_row_num=1，默认第1行为开始，直接输入目标行即可
first_row_num   sheet中目标行的行数
first_row_list  sheet中第一行的名称列表，每一列的意义

#获取target_sheet的某一列的值    涉及到的方法  get_target_sheet_col_list 输入参数col_name=None,输入列名
self.target_sheet_col_names
self.target_sheet_col_value_list=None

"""
class Excel_file(object):
    def __init__(self,path):
        #输入参数
        self.path=path
        #开始读取excel表格
        self.workbook = xlrd.open_workbook(self.path, encoding_override='utf-8')

        #获取excel表格sheet的相关参数
        self.sheet_names = self.get_sheet_names()
        self.sheet_num = self.get_sheet_num()

        # 执行get_target_sheet方法后，获得target_sheet
        self.target_sheet=None
        self.target_sheet_rows=None
        self.target_sheet_cols=None

        #执行方法，获取分类第一排的列表
        self.first_row_num=0
        self.first_row_list = None

        #执行方法，获取相应的列的值
        self.target_sheet_col_names=None
        self.target_sheet_col_value_list=None

        #执行方法，获取相应的行的值
        self.target_row_value_list=None


    #获取excel表格全部sheets的列表
    def get_sheet_names(self):
        return self.workbook.sheet_names()

    #获取excel表格全部sheets的数量
    def get_sheet_num(self):
        return self.workbook.nsheets

    #获取excel表格中指定的sheet
    def get_target_sheet(self,target_sheet_name=None):
        sheet_name=target_sheet_name
        #如果输入sheet名称在excel文件sheet里面，则直接选择该sheet
        for i in self.sheet_names:
            if sheet_name == i:
                self.target_sheet=self.workbook.sheet_by_name(sheet_name)
            elif sheet_name in i:
                self.target_sheet=self.workbook.sheet_names(i)
            else:
                pass
        self.target_sheet_rows=self.target_sheet.nrows
        self.target_sheet_cols=self.target_sheet.ncols

    #获取sheet中真正意义上的第一排数据
    #默认读取第一行数据
    def get_first_row_list(self,first_row_num=1):
        self.first_row_num=first_row_num-1
        self.first_row_list=list(self.target_sheet.row_values(self.first_row_num))
        self.target_sheet_col_names=self.first_row_list

    #获取sheet中的指定列的值，从目标行往下，一直到最后一列
    def get_target_sheet_col_list(self,col_name=None):
        self.target_sheet_col_name=col_name
        for i in self.first_row_list:
            if col_name in i:
                self.target_sheet_col_num=self.first_row_list.index(i)
        self.target_sheet_col_value_list=list(self.target_sheet.col_values(self.target_sheet_col_num, start_rowx=self.first_row_num+1))

    #获取sheet中的指定行的值，每一行的所有值都获取
    def get_target_sheet_row_list(self,row_num):
        row_num=row_num-1
        self.target_row_value_list=list(self.target_sheet.row_values(row_num))



#试验用
e=Excel_file(path=path)
e.get_target_sheet(target_sheet_name="故障填报主表")
e.get_first_row_list(first_row_num=3)
e.get_target_sheet_col_list(col_name="分公司名称")
e.get_target_sheet_row_list(row_num=100)
print(e.sheet_names)
print("-----")
print(e.sheet_num)
print("-----")
print(e.target_sheet_rows)
print("----")
print(e.target_sheet_cols)
print("----")
print(e.first_row_list)
print("----")
print(len(e.target_sheet_col_value_list))
print("----")
print(e.target_row_value_list)
