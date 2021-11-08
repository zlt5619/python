from PyQt5.QtWidgets import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("内置信号和自定义槽函数示例")
        self.resize(300,200)
        btn=QPushButton('关闭',self)
        btn.clicked.connect(self.btn_close)

    def btn_close(self):
        print("关闭窗口")
        self.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())