from PyQt5.QtCore import QObject,pyqtSignal

#信号对象
class QTypeSignal(QObject):
    #定义一个信号
    sendMsg=pyqtSignal(str,str)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        #发射信号
        self.sendMsg.emit("Hello pyqt5","第二个参数")

#槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self,msg1,msg2):
        print("QSlot get msg1: => "+msg1)
        print("QSlot get msg2: => "+msg2)

if __name__=="__main__":
    send=QTypeSignal()
    slot=QTypeSlot()

    print("---把信号绑定到槽函数上---")
    send.sendMsg.connect(slot.get)
    send.run()

    print("---把信号和槽函数的连接断开---")
    send.sendMsg.disconnect(slot.get)
    send.run()