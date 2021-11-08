import sys
from PyQt5.QtWidgets import *

class Radiodemo(QWidget):
    def __init__(self,parent=None):
        super(Radiodemo, self).__init__(parent)
        layout=QHBoxLayout()
        self.btn1=QRadioButton("Button1")
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda : self.btnstate(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2=QRadioButton("Button2")
        self.btn2.toggled.connect(lambda : self.btnstate(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.setWindowTitle("RadioButton Demo")

    def btnstate(self,btn):
        if btn.text()=="Button1":
            print("Button1 is selected")
        else:
            print("Button1 is not selected")
        if btn.text()=="Button2":
            print("Button2 is selected")
        else:
            print("Button2 is not selected")

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Radiodemo()
    win.show()
    sys.exit(app.exec_())
