"""
对单一窗口的程序，一个控件的变化会影响另一个控件的变化，利用信号与槽
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #先场建滑块和LCD控件
        lcd=QLCDNumber(self)
        slider=QSlider(Qt.Horizontal,self)

        vBox=QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)

        self.setLayout(vBox)

        #valueChanged()是slider的一个信号函数，只要slider的值发生改变，就会发出一个信号，然后通过connect连接信号接受的控件，也就是LCD

        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,350,150)
        self.setWindowTitle("连接滑块LCD")

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())