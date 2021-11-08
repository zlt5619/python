from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
import sys

class LineEditDemo(QWidget):
    def __init__(self,parent=None):
        super(LineEditDemo,self).__init__(parent)
        self.setWindowTitle("QLineEdit例子")

        flo=QFormLayout()

        pNormalLineEdit=QLineEdit()
        pNoEchoLineEdit=QLineEdit()
        pPasswordLineEdit=QLineEdit()
        pPasswordEchoOnEditLine=QLineEdit()

        flo.addRow("Normal",pNormalLineEdit)
        flo.addRow("NoEcho",pNoEchoLineEdit)
        flo.addRow("Password",pPasswordLineEdit)
        flo.addRow("PasswordEcho",pPasswordEchoOnEditLine)

        pNormalLineEdit.setPlaceholderText("Normal")
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("Password")
        pPasswordEchoOnEditLine.setPlaceholderText("PasswordEcho")

        self.setLayout(flo)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=LineEditDemo()
    win.show()
    sys.exit(app.exec_())
