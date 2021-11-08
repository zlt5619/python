from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSignal,Qt
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 355)
        self.controlGrooup = QtWidgets.QGroupBox(Form)
        self.controlGrooup.setGeometry(QtCore.QRect(20, 100, 431, 141))
        self.controlGrooup.setObjectName("controlGrooup")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.controlGrooup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 411, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberspinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.numberspinBox.setObjectName("numberspinBox")
        self.horizontalLayout.addWidget(self.numberspinBox)
        self.styleCombo = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.horizontalLayout.addWidget(self.styleCombo)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.printButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.controlGrooup)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewStatus = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.previewStatus.setObjectName("previewStatus")
        self.horizontalLayout_2.addWidget(self.previewStatus)
        self.previewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.resultGroup = QtWidgets.QGroupBox(Form)
        self.resultGroup.setGeometry(QtCore.QRect(450, 100, 351, 141))
        self.resultGroup.setObjectName("resultGroup")
        self.result_label = QtWidgets.QLabel(self.resultGroup)
        self.result_label.setGeometry(QtCore.QRect(13, 59, 321, 31))
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.controlGrooup.setTitle(_translate("Form", "打印控制"))
        self.label.setText(_translate("Form", "打印份数："))
        self.styleCombo.setItemText(0, _translate("Form", "A4"))
        self.styleCombo.setItemText(1, _translate("Form", "A3"))
        self.styleCombo.setItemText(2, _translate("Form", "A2"))
        self.label_2.setText(_translate("Form", "纸张类型："))
        self.printButton.setText(_translate("Form", "打印"))
        self.previewStatus.setText(_translate("Form", "全屏显示"))
        self.previewButton.setText(_translate("Form", "预览"))
        self.resultGroup.setTitle(_translate("Form", "操作结果"))


class MyMainWindow(QMainWindow,Ui_Form):
    #创建需要传递的信号
    helpSignal=pyqtSignal(str)
    printSignal=pyqtSignal(list)
    #创建一个重载信号，包括int和str 以及str类 的参数
    previewSignal=pyqtSignal([int,str],[str])

    def __init__(self,parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    #配置信号和槽函数
    def initUI(self):
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int,str].connect(self.previewPaperWithArg)

        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

    #发射预览信息
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked()==True:
            self.previewSignal[int,str].emit(1080,"Full Screen")
        else:
            self.previewSignal[str].emit("Preview")


    #发射打印信号
    def emitPrintSignal(self):
        pList=[]
        pList.append(self.numberspinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    def printPaper(self,list):
        str1=str(list[0])
        str2=str(list[1])
        all_str="打印：份数："+str1+"  纸张："+str2
        self.result_label.setText(all_str)

    def previewPaperWithArg(self,style,text):
        self.result_label.setText("打印尺寸："+str(style)+" 显示："+text)

    def previewPaper(self,text):
        self.result_label.setText(text)

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_F1:
            self.helpSignal.emit("help message")

    def showHelpMessage(self,message):
        self.result_label.setText(message)
        self.statusBar().showMessage(message)



if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MyMainWindow()
    win.show()
    sys.exit(app.exec_())