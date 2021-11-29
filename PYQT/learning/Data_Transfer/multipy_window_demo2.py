"""
对单一窗口的程序，一个控件的变化会影响另一个控件的变化，利用信号与槽
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DateDialog(QDialog):
    Signal_OneParameter=pyqtSignal(str)

    def __init__(self,parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("子窗口")

        #在布局中添加控件
        layout=QVBoxLayout(self)

        self.label=QLabel(self)
        self.label.setText("前者发射内置信号\n后者发射自定义信号")

        self.datetime_inner=QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit=QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)
        layout.addWidget(self.label)

        buttons=QDialogButtonBox(
            QDialogButtonBox.Ok|QDialogButtonBox.Cancel,
            Qt.Horizontal,self
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.rejiect)
        layout.addWidget(buttons)

        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)

    def emit_signal(self):
        date_str=self.datetime_emit.dateTime().toString()
        self.Signal_OneParameter.emit(date_str)


class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400,90)
        self.setWindowTitle("信号与槽传递参数的示例")

        self.open_btn=QPushButton("获取时间")
        self.lineEdit_inner=QLineEdit(self)
        self.lineEdit_emit=QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_emit.setText("接受子窗口自定义信号的时间")
        self.lineEdit_inner.setText("接受子窗口内置的时间")

        grid=QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        grid.addWidget(self.open_btn)

        self.setLayout(grid)

    def openDialog(self):
        dialog=DateDialog(self)
        # dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)

        # dialog.Signal_OneParameter.connect(self.deal_emit_slot)

        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self,datestr):
        self.lineEdit_emit.setText(datestr)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())