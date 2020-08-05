#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter


top = tkinter.Tk()


def helloCallBack():
    print("123")


B = tkinter.Button(top, text="点我", command=helloCallBack)

B.pack()
top.mainloop()