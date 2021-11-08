import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class CustomSignal(QWidget):

    #声明无参数变量
    signal1=pyqtSignal()
    #声明一个int参数变量
    signal2=pyqtSignal(int)
    #声明两个int和str参数变量
    signal3=pyqtSignal(int,str)
    #声明列表参数变量
    signal4=pyqtSignal(list)
    #声明列字典参数变量
    signal5=pyqtSignal(dict)
    #声明列多重载，包括int和str以及带str类型的参数变量
    signal6=pyqtSignal([int,str],[str])

    def __init__(self,parent=None):
        super(CustomSignal, self).__init__(parent)

        #将信号连接至槽函数
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int,str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6Overload)

        #发射信号
        self.signal1.emit()
        self.signal2.emit(23)
        self.signal3.emit(5,"hello")
        self.signal4.emit(['a','b','c'])
        self.signal5.emit({1:2,2:4,4:8})
        self.signal6[int,str].emit(6,'world')
        self.signal6[str].emit('world')

    def signalCall1(self):
        print("signal1 emit")
    def signalCall2(self,value):
        print("signal2 emit:",value)
    def signalCall3(self,value,text):
        print("signal3 emit:",value,text)
    def signalCall4(self,value):
        for i in value:
            print(i+"------")
    def signalCall5(self,value):
        print("signal5 emit:",value)
    def signalCall6(self,val,text):
        print("signal 6 emit:",val,text)
    def signalCall6Overload(self,value):
        print("signal 6 overload emit:",value)

if __name__=="__main__":
    app=QApplication(sys.argv)
    customsignal=CustomSignal()
    sys.exit(app.exec_())