from tkinter import Tk, Frame, Button, Label, Entry, StringVar
from tkinter.filedialog import askopenfilenames
from pyautocad import Autocad
import xlrd
#输入文件路径，用于比较
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
        B3 = Button(self, text="比较CAD文件", command=lambda: self.compare(self.filelist), height=1)
        B3.grid(row=2, column=1, padx=3)

    def selectPath(self, path1):
        path_ = askopenfilenames()
        path1.set(path_)
        self.filelist = []
        self.filelist.append(path_)

    def checkInput(self):
        L2 = Label(self, text="√")
        L2.grid(row=1, column=4, padx=3)

    def compare(self,filelist):
        obj=acad.iter_objects("Text")
        for i in obj:
            self.text_list[i.TextString]=[i.InsertionPoint,i.Height,i]
        excel_file=self.read_excel(self.filelist)
        famen=[]
        fangjianhao=[]
        pair=dict()
        #判断谁在excel文件里，形成阀门列表
        for key in self.text_list.keys():
            if key in excel_file.keys():
                famen.append(key)
            else:
                fangjianhao.append(key)
        for i in famen:
            i_y=self.text_list[i][0][1]
            i_height=self.text_list[i][1]
            for j in fangjianhao:
                j_y=self.text_list[j][0][1]
                if i_y-2*i_height<j_y and j_y<i_y+2*i_height:
                    pair[i]=j
        # print(pair)
        # print(excel_file)

        #修改cad过程
        xiugai=[]
        for key in excel_file.keys():
            if excel_file[key]==pair[key]:
                pass
            else:
                xiugai.append(key)
        flag=0
        for key in xiugai:
            old_value = pair[key]
            new_value = excel_file[key]
            if old_value==new_value:
                pass
            else:
                flag=1
        if flag==1:
            for key in xiugai:
                old_value=pair[key]
                new_value=excel_file[key]
                obj=self.text_list[old_value][2]
                obj.TextString=new_value
        else:
            root1=Tk(className="结果")
            root1.geometry("300x100")
            l1=Label(root1,text="完全正确")
            l1.pack()
            root1.mainloop()
    def read_excel(self,filelist):
        filelist=filelist[0][0]
        result=dict()
        data = xlrd.open_workbook(filelist)
        table = data.sheet_by_index(0)
        for i in range(3):
            row=table.row_values(i)
            result[row[0]]=row[1]
        return result
if __name__=="__main__":
    acad = Autocad(create_if_not_exists=True)
    root=Tk(className="demo1")
    root.geometry("500x200")
    ip_frame=input_Frame(root)
    ip_frame.pack()
    root.mainloop()
