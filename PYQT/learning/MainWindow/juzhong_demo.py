import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.setWindowTitle("主窗口放在屏幕中间")
        self.resize(1000,500)
        self.center()

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

if __name__=="__main__":
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())