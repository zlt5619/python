import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.resize(400,200)
        self.status=self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)
        self.setWindowTitle("PyQt MainWindow例子")

if __name__=="__main__":
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())