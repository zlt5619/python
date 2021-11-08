
class strProcess(object):
    def __init__(self):
        self.str=input()
        self.process_str()
        self.check_str()
        self.final_list=[]
        self.print_list()
        self.final_list.sort()
        print(self.final_list)

    def process_str(self):
        self.raw_list=self.str.split(' ')
        self.str_num=self.raw_list[0]

    def check_str(self):
        if int(self.raw_list[0])!=(len(self.raw_list)-1):
            print("请重新输入字符串")
            self.str = input()
        for i in range(len(self.raw_list)):
            if i==0:
                pass
            else:
                if len(self.raw_list[i])>100:
                    print("请重新输入字符串")
                    self.str=input()

    def print_list(self):
        self.printlist=[]
        self.need_process_list=[]
        for i in range(len(self.raw_list)):
            if i==0:
                pass
            else:
                self.printlist.append(self.raw_list[i])
        for i in self.printlist:
            if len(i)<=8:
                for j in range(8-len(i)):
                    i+='0'
                self.final_list.append(i)
            else:
                self.need_process_list.append(i)
        for i in self.need_process_list:
            a=len(i)
            count=int(a/8)
            yushu=a%8
            list1=list(i)
            yushu_str=""
            for i in range(count):
                str=list1[0+i*8]+list1[1+i*8]+list1[2+i*8]+list1[3+i*8]+list1[4+i*8]+list1[5+i*8]+list1[6+i*8]+list1[7+i*8]
                self.final_list.append(str)
            for j in range(yushu):
                yushu_str+=list1[j+count*8]
            for j in range(8 - len(yushu_str)):
                yushu_str += '0'
            self.final_list.append(yushu_str)



a=strProcess()

