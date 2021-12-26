"""
展示用，通过GUI输入一个路径
1、判断是文件，还是路径
2、是文件，弹出messagebox，提示是文件
3、是路径，弹出新窗口，提示生成excel文件，展示该路径下的文件结构，文件类型
"""
from tkinter import *
from tkinter.filedialog import *
import xlwt

class processdir2():
    def __init__(self,dir=None):
        self.dir=dir
        self.filelists=[]
        self.process()

    def process(self,dir=None):
        if dir==None:
            raw_list=os.listdir(self.dir)
            for i in raw_list:
                if os.path.isdir(self.dir+"/"+i):
                    str1=self.dir+"/"+i
                    self.process(dir=str1)
                else:
                    self.filelists.append(i)
        else:
            raw_list=os.listdir(dir)
            for i in raw_list:
                if os.path.isdir(dir+"/"+i):
                    str1=dir+"/"+i
                    self.process(dir=str1)
                else:
                    self.filelists.append(i)

class processdir(object):
    def __init__(self,dir=None):
        self.dir=dir
        self.content=[dir]
        self.process()

    def process(self,dir=None):
        if dir==None:
            raw_list=os.listdir(self.dir)
            for i in raw_list:
                if os.path.isdir(self.dir+"/"+i):
                    self.content.append(self.dir+"/"+i)
                    self.process(dir=self.dir+"/"+i)
        else:
            raw_list = os.listdir(dir)
            for i in raw_list:
                if os.path.isdir(dir + "/" + i):
                    self.content.append(dir + "/" + i)
                    self.process(dir=dir + "/" + i)

class process_frame(Frame):
    def __init__(self,root=None,path=None):
        super().__init__(root)
        self.path=path
        B1 = Button(self, text="生成文件路径结构Excel", command=lambda: self.makefilepathexcel(), height=1)
        B1.grid(row=0, column=1,padx=10,pady=20)
        B2 = Button(self, text="生成文件类型分类Excel", command=lambda: self.makefilekindexcel(), height=1)
        B2.grid(row=0, column=2,padx=10,pady=20)
        self.processdirectory()


    def makefilepathexcel(self):
        save_path=askdirectory()
        self.all_dir=[]
        for i in self.dirpath:
            list1=i.split("/")
            self.all_dir.append(list1)
        self.all_dir.pop(0)
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('文件路径结构')
        row_value=[]
        for i in range(100):
            row_value.append(0)
        for i in range(len(self.all_dir)):
            for j in range(len(self.all_dir[i])):
                if self.all_dir[i][j]==row_value[j]:
                    worksheet.write(i, j, '')
                else:
                    worksheet.write(i, j, self.all_dir[i][j])
                    row_value[j]=self.all_dir[i][j]
        workbook.save(save_path+'/文件路径结构.xls')


    def makefilekindexcel(self):
        save_path = askdirectory()
        self.write_material= {'无后缀名文件':[]}
        for i in self.filelists:
            if '.' in i:
                strs=i.split('.')
                self.write_material[strs[-1].lower()]=[]
        for i in self.filelists:
            if '.' in i:
                strs=i.split('.')
                self.write_material[strs[-1].lower()].append(i)
            else:
                self.write_material['无后缀名文件'].append(i)
        workbook = xlwt.Workbook(encoding='ascii')
        for i in self.write_material.keys():
            worksheet=workbook.add_sheet(i)
            list1=self.write_material[i]
            worksheet.write(0, 0, '序号')
            worksheet.write(0,1,'文件名')
            for j in range(len(list1)):
                worksheet.write(j+1,0,j+1)
                worksheet.write(j+1,1,list1[j])
        workbook.save(save_path + '/文件名称.xls')

    def processdirectory(self):
        self.dirpath=processdir(dir=self.path).content
        self.filelists=processdir2(dir=self.path).filelists




class input_file_frame(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.path1 = StringVar()
        self.filepath=None
        L1 = Label(self, text="请选择任意的文件路径:")
        L1.grid(row=0, column=0,pady=30,padx=20)
        E1 = Entry(self, textvariable=self.path1, width=30)
        E1.grid(row=0, column=1,pady=30)
        # command 后面的函数不能有参数，否则会直接执行，跳出文本选择框，需要在函数前加lambda，变成匿名函数
        B1 = Button(self, text="...", command=lambda: self.selectPath(), height=1)
        B1.grid(row=0, column=2, padx=10,pady=30)
        B2=Button(self, text="处理文件路径", command=lambda: self.processPath(), height=1)
        B2.grid(row=1, column=1)

    def selectPath(self):
        path_ = askdirectory()
        self.path1.set(path_)
        self.filepath = path_

    def processPath(self):
        root1=Tk(className="请选择处理路径的方式")
        root1.geometry("350x80")
        p_frame=process_frame(root=root1,path=self.filepath)
        p_frame.pack()
        root1.mainloop()

if __name__=="__main__":
    root = Tk(className="文件路径的处理")
    root.geometry("500x150")
    if_frame = input_file_frame(root)
    if_frame.pack()
    root.mainloop()