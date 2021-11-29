#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter


top = tkinter.Tk()


def print_positon(Button):
    Button.place(x=200,y=100)
    print(Button.cget("text"))


B = tkinter.Button(top, text="点我", command=lambda :print_positon(B))

B.place(x=100,y=100)


# print(B.place_info())
# print(type(B.place_info()))
# print(B.place_info()["x"])
# print(B.place_info()["y"])

top.mainloop()