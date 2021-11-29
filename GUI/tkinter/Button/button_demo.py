#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter


top = tkinter.Tk()


def helloCallBack(button=None):
    b=button
    print(b)


B = tkinter.Button(top, text="点我", command=lambda :helloCallBack())

B.pack()
top.mainloop()