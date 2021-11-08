from PyQt5.QtCore import QObject,pyqtSignal

#信号对象
class QTypeSignal(QObject):
    #定义一个信号
    sendMsg=pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        #发射信号
        self.sendMsg.emit("Hello pyqt5")

#槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self,msg):
        print("QSlot get msg: => "+msg)

if __name__=="__main__":
    send=QTypeSignal()
    slot=QTypeSlot()

    print("---把信号绑定到槽函数上---")
    send.sendMsg.connect(slot.get)
    send.run()

    print("---把信号和槽函数的连接断开---")
    send.sendMsg.disconnect(slot.get)
    send.run()