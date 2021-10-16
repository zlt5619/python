import xlrd

path="C:/Users/zlt/Desktop/田祥资料/03 湖北分公司月度故障分析(图表)-2021年09月.xlsx"

#定义excel文件类，输入excel文件路径，得到该excel的全部内容
class Excel_File(object):
    def __init__(self,path):
        #读取excel表格
        self.workbook=xlrd.open_workbook(path,encoding_override='utf-8')
        self.sheetnames=self.get_all_sheetnames()
        self.target_sheet = self.get_target_sheet()
        self.sheet_rows=self.get_target_rows()
        self.get_target_sheet_col_name()
        self.fengdianchang_name=self.get_all_fengdianchang_name()
        self.jizuzongshu=self.get_all_fengdianchang_jizu_num()


    #获取excel表格中的所有sheet名字
    def get_all_sheetnames(self):
        return self.workbook.sheet_names()

    #获取相关的sheet
    def get_target_sheet(self):
        #如果sheet的名字里含有故障，则选定该sheet
        for sheetname in self.sheetnames:
            if "故障汇总" in sheetname:
                self.target_sheet_name=sheetname
        target_sheet=self.workbook.sheet_by_name(self.target_sheet_name)
        return target_sheet

    #找到相对应的sheet后，确认它的行数
    def get_target_sheet_rows(self):
        rows=self.target_sheet.nrows
        return rows

    #找到相对应的sheet后，确认它的列数
    def get_target_sheet_cols(self):
        cols=self.target_sheet.ncols
        return cols

    #找到相对应的sheet后，确认它第一列的名称
    def get_target_sheet_col_name(self):
        self.first_col_names=list(self.target_sheet.row_values(0))
        return self.first_col_names

    #根据所需名称，读取相关一竖列的所有数据
    def get_target_col_value(self,name):
        target_col_num=0
        for i in range(len(self.first_col_names)):
            if self.first_col_names[i]==name:
                target_col_num=i
        #从第2排开始读数
        target_col_value=self.target_sheet.col_values(target_col_num,1)
        return target_col_value

    #读取所有风机场名称
    def get_all_fengdianchang_name(self):
        fengdianchang_list=self.get_target_col_value("风电场")
        fengdianchang_set=set(fengdianchang_list)
        fengdianchang_set.remove('')
        fengdianchang_list=list(fengdianchang_set)
        return fengdianchang_list


    #读取风电场机组台数
    def get_all_fengdianchang_jizu_num(self):
        jizuzongshu_dict=dict()
        fengdianchang_list=self.get_target_col_value("风电场")
        jizuzongshu_list=self.get_target_col_value("机组总数")
        for i in range(len(fengdianchang_list)):
            if fengdianchang_list[i]=='':
                pass
            else:
                jizuzongshu_dict[fengdianchang_list[i]]=jizuzongshu_list[i]
        return jizuzongshu_dict

    #根据某一列的值，选定所有的行
    def get_target_rows(self,col_num=0,col_value=''):
        target_rows=[]
        for i in range(1,self.sheet_rows):
            if self.target_sheet.row_values(i)[col_num]==col_value:
                target_rows.append(self.target_sheet.row_values(i))
        return target_rows


e=Excel_File(path)
sheet=e.get_target_sheet()
c=e.get_target_rows(col_num=8,col_value='故障停机')
# print(sheet.name)
print(c)


