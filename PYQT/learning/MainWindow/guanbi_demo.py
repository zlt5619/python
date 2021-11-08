import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.resize(500,300)
        self.setWindowTitle("关闭主窗口")
        self.button1=QPushButton("关闭主窗口")
        self.button1.clicked.connect(self.onButtonClick)

        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame=QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        #sender 是发送信号的对象
        sender=self.sender()
        print(sender.text()+"被按下了")
        """
        获得QApplication类的对象，调用quit()方法，从而关闭窗口
        """
        qApp=QApplication.instance()
        qApp.quit()



if __name__=="__main__":
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())