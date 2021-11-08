import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog

    #为生成的代码段
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closeWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeWinBtn.setGeometry(QtCore.QRect(250, 170, 75, 23))
        self.closeWinBtn.setObjectName("closeWinBtn")
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

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.filecloseAction.triggered.connect(self.close)
        self.fileopenaction.triggered.connect(self.openMsg)

    def openMsg(self):
        file,ok=QFileDialog.getOpenFileNames(self,"打开","C:/","All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())
