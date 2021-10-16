from tkinter import *
from tkinter.filedialog import askopenfilenames
import xlrd

"""
1、需要考虑不同frame之间的数据传递问题，因为是mainloop循环，要点button，才能把数据成功传递出去
"""


if __name__=="__main__":
    root= Tk(className="试验用")
    root.geometry("500x300")
    """
    添加想要加载的模块
    试验想要的效果，root为最基础的框架
    """
    root.mainloop()