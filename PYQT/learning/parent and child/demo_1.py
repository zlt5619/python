import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog

#为生成的代码段
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closeWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeWinBtn.setGeometry(QtCore.QRect(250, 370, 75, 23))
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 60, 321, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileopenaction = QtWidgets.QAction(MainWindow)
        self.fileopenaction.setObjectName("fileopenaction")
        self.fileNewAction = QtWidgets.QAction(MainWindow)
        self.fileNewAction.setObjectName("fileNewAction")
        self.addwinaction = QtWidgets.QAction(MainWindow)
        self.addwinaction.setObjectName("addwinaction")
        self.filecloseAction = QtWidgets.QAction(MainWindow)
        self.filecloseAction.setObjectName("filecloseAction")
        self.menu.addAction(self.fileopenaction)
        self.menu.addAction(self.fileNewAction)
        self.menu.addAction(self.filecloseAction)
        self.menu_2.addAction(self.addwinaction)
        self.menu_2.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.addwinaction)

        self.retranslateUi(MainWindow)
        self.closeWinBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeWinBtn.setText(_translate("MainWindow", "关闭窗口"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.fileopenaction.setText(_translate("MainWindow", "打开"))
        self.fileopenaction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.fileNewAction.setText(_translate("MainWindow", "新建"))
        self.fileNewAction.setShortcut(_translate("MainWindow", "Alt+N"))
        self.addwinaction.setText(_translate("MainWindow", "添加窗口"))
        self.addwinaction.setToolTip(_translate("MainWindow", "添加窗口"))
        self.filecloseAction.setText(_translate("MainWindow", "关闭"))
        self.filecloseAction.setShortcut(_translate("MainWindow", "Alt+C"))

class Ui_ChildForm(object):
    def setupUi(self, ChildForm):
        ChildForm.setObjectName("ChildForm")
        ChildForm.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(ChildForm)
        self.textEdit.setGeometry(QtCore.QRect(70, 60, 251, 151))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildForm)
        QtCore.QMetaObject.connectSlotsByName(ChildForm)

    def retranslateUi(self, ChildForm):
        _translate = QtCore.QCoreApplication.translate
        ChildForm.setWindowTitle(_translate("ChildForm", "child_Form"))
        self.textEdit.setHtml(_translate("ChildForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我是子窗口</p></body></html>"))

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.child=ChildForm()
        self.filecloseAction.triggered.connect(self.close)
        self.fileopenaction.triggered.connect(self.openMsg)
        self.addwinaction.triggered.connect(self.childShow)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileNames(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

class ChildForm(QMainWindow,Ui_ChildForm):
    def __init__(self):
        super(ChildForm,self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win=MainForm()
    win.show()
    sys.exit(app.exec_())
