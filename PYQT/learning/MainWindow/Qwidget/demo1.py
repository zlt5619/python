from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

app=QApplication(sys.argv)
widget=QWidget()
btn=QPushButton(widget)
btn.setText("Button123")
btn.move(20,20)
widget.resize(300,200)

widget.move(250,200)

widget.setWindowTitle("PyQt坐标系统例子")
widget.show()

sys.exit(app.exec_())