from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

class Icon(QWidget):
    def __init__(self,parent=None):
        super(Icon,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('程序图标')
        self.setWindowIcon(QIcon("./aaa.ico"))

if __name__=="__main__":
    app=QApplication(sys.argv)
    icon=Icon()
    icon.show()
    sys.exit(app.exec_())