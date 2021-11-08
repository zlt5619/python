from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

class WinForm(QWidget):

    #自定义信号，不带参数
    button_click_signal=pyqtSignal()

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("custom signal and slot")
        self.resize(330,50)
        btn=QPushButton("close",self)
        btn.clicked.connect(self.btn_clicked)
        self.button_click_signal.connect(self.close)

    def btn_clicked(self):
        print("按钮按下，传递至自定义的信号")
        self.button_click_signal.emit()

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())