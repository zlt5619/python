from PyQt5.QtWidgets import *
import sys

class WinForm(QMainWindow):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        button1=QPushButton("button1")
        button2=QPushButton("button2")

        button1.clicked.connect(lambda :self.onButtonClick(1))
        button2.clicked.connect(lambda :self.onButtonClick(2))

        layout=QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame=QWidget()
        
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self,val):
        print('Button {0} 被按下了'.format(val))
        QMessageBox.information(self,"信息提示器",'Button {0} 被按下了'.format(val))

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())