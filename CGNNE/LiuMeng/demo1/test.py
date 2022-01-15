import datetime
from tkinter import Tk, Frame, StringVar, Label, Entry, Button
from tkinter.filedialog import askopenfilename

import xlrd





class Select_Frame(Frame):
    def __init__(self, root=None, generator_list=None):
        super().__init__(root)
        self.generator_list = generator_list
        self.path1 = StringVar()
        self.path2 = StringVar()
        self.path3 = StringVar()
        self.path4 = StringVar()
        self.path5 = StringVar()
        self.path6 = StringVar()
        self.path7 = StringVar()
        self.path8 = StringVar()
        self.path9 = StringVar()
        self.path10 = StringVar()
        L1 = Label(self, text="输入起始时间")
        L1.grid(row=0, column=2)
        L2=Label(self,text="年")
        L2.grid(row=1, column=0,padx=5)
        L3 = Label(self, text="月")
        L3.grid(row=1, column=1,padx=5)
        L4 = Label(self, text="日")
        L4.grid(row=1, column=2,padx=5)
        L5 = Label(self, text="时")
        L5.grid(row=1, column=3,padx=5)
        L6 = Label(self, text="分")
        L6.grid(row=1, column=4,padx=5)
        E1 = Entry(self, textvariable=self.path1, width=4)
        E1.grid(row=2, column=0)
        E2 = Entry(self, textvariable=self.path2, width=4)
        E2.grid(row=2, column=1)
        E3 = Entry(self, textvariable=self.path3, width=4)
        E3.grid(row=2, column=2)
        E4 = Entry(self, textvariable=self.path4, width=4)
        E4.grid(row=2, column=3)
        E5 = Entry(self, textvariable=self.path5, width=4)
        E5.grid(row=2, column=4)

        L7 = Label(self, text="输入终止时间")
        L7.grid(row=3, column=2)
        L8 = Label(self, text="年")
        L8.grid(row=4, column=0, padx=5)
        L9 = Label(self, text="月")
        L9.grid(row=4, column=1, padx=5)
        L10 = Label(self, text="日")
        L10.grid(row=4, column=2, padx=5)
        L11 = Label(self, text="时")
        L11.grid(row=4, column=3, padx=5)
        L12 = Label(self, text="分")
        L12.grid(row=4, column=4, padx=5)
        E6 = Entry(self, textvariable=self.path6, width=4)
        E6.grid(row=5, column=0)
        E7 = Entry(self, textvariable=self.path7, width=4)
        E7.grid(row=5, column=1)
        E8 = Entry(self, textvariable=self.path8, width=4)
        E8.grid(row=5, column=2)
        E9 = Entry(self, textvariable=self.path9, width=4)
        E9.grid(row=5, column=3)
        E10 = Entry(self, textvariable=self.path10, width=4)
        E10.grid(row=5, column=4)
        B1 = Button(self, text="生成折线图", command=lambda: self.draw_picture(), height=1)
        B1.grid(row=6, column=2, padx=10, pady=30)

    def draw_picture(self):
        str1=int(self.children['!entry'].get())
        str2=int(self.children['!entry2'].get())
        str3=int(self.children['!entry3'].get())
        str4=int(self.children['!entry4'].get())
        str5=int(self.children['!entry5'].get())
        str6=int(self.children['!entry6'].get())
        str7=int(self.children['!entry7'].get())
        str8=int(self.children['!entry8'].get())
        str9=int(self.children['!entry9'].get())
        str10=int(self.children['!entry10'].get())
        start_time=datetime.datetime(str1,str2,str3,str4,str5)
        end_time=datetime.datetime(str6,str7,str8,str9,str10)
        if self.istimecorrect(start_time,end_time):
            print(self.start_id)
            print(self.end_id)
        else:
            L13 = Label(self, text="输入时间有误，请重新输入")
            L13.grid(row=7, column=2)
    def istimecorrect(self,start_time,end_time):
        self.start_id=None
        self.end_id=None
        for i in self.generator_list:
            if start_time==i[1]:
                self.start_id=i[0]
            if end_time==i[1]:
                self.end_id=i[0]
        if self.start_id==None or self.end_id==None:
            return False
        else:
            return True


root=Tk(className="123")
root.geometry("300x400")
frame=Select_Frame(root,generator_list=None)
frame.pack()
root.mainloop()