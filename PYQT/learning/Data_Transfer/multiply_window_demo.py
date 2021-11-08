"""
对单一窗口的程序，一个控件的变化会影响另一个控件的变化，利用信号与槽
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400,90)
        self.setWindowTitle("传值回主窗口")

        self.lineEdit=QLineEdit(self)
        self.button1=QPushButton("弹出对话框1")
        self.button1.clicked.connect(self.onButton1Click)

        self.button2=QPushButton("弹出对话框2")
        self.button2.clicked.connect(self.onButton2Click)

        gridlayout=QGridLayout()
        gridlayout.addWidget(self.lineEdit)
        gridlayout.addWidget(self.button1)
        gridlayout.addWidget(self.button2)
        self.setLayout(gridlayout)

    def onButton1Click(self):
        dialog=DateDialog(self)
        result=dialog.exec_()
        date=dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n日期对话框的返回值')
        print('date=%s'%str(date.date()))
        print("time-%s"%str(date.time()))
        print("result=%s"%result)
        dialog.destroy()

    def onButton2Click(self):
        date,time,result=DateDialog.getDateTime()
        self.lineEdit(date.toString())
        print('\n日期对话框的返回值')
        print('date=%s' % str(date.date()))
        print("time-%s" % str(date.time()))
        print("result=%s" % result)

class DateDialog(QDialog):
    def __init__(self,parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("DateDialog")
        self.resize(200,50)

        layout=QVBoxLayout()
        self.datetime=QDateTimeEdit(self)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        #使用ok和cancel连接accept()和reject()槽函数
        buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    #使用静态函数创建对话框并返回（date，time，accepted）
    @staticmethod
    def getDateTime(parent=None):
        dialog=DateDialog(parent)
        result=dialog.exec_()
        date=dialog.dateTime()
        return (date.date(),date.time(),result==QDialog.Accepted)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())