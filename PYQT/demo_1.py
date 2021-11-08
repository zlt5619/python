# -*- coding:UTF-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#为生成的代码段
class Ui_MainWindow(object):
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
