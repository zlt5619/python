import tkinter as tk
import tkinter.messagebox as msg
"""
动态创建多个按钮，如何解决参数问题
"""

# def cbClicked(cbname):
#     for cb in cb_group:
#         cb_group[cb]["cbobj"]["fg"] = "red" if cb == cbname else "black"
#     # msg.showinfo('您点击了', cbname)
#
#
# cb_group = {
#     "cb1": {'cbname': "按钮1", 'cbobj': None},
#     "cb2": {'cbname': "按钮2", 'cbobj': None},
#     "cb3": {'cbname': "按钮3", 'cbobj': None}
# }
#
# win = tk.Tk()
#
# for inx, cb in enumerate(cb_group):
#     b = tk.Button(win, width=10, height=1, text=cb_group[cb]["cbname"])
#     b["command"] = lambda arg=cb: cbClicked(arg)
#     b.grid(row=0, column=inx)
#     cb_group[cb]["cbobj"] = b
#     print(inx)
#     print(cb)
#
# win.mainloop()

from tkinter import Tk, Button, GROOVE

root = Tk()

def appear(index, letter):
    # This line would be where you insert the letter in the textbox
    print (letter)

    # Disable the button by index
    buttons[index].config(state="disabled")

letters=["A", "T", "D", "M", "E", "A", "S", "R", "M"]

# A collection (list) to hold the references to the buttons created below
buttons = []

for index in range(9):
    n=letters[index]

    button = Button(root, bg="White", text=n, width=5, height=1, relief=GROOVE,
                    command=lambda index=index, n=n: appear(index, n))

    # Add the button to the window
    button.grid(padx=2, pady=2, row=index, column=0)

    # Add a reference to the button to 'buttons'
    buttons.append(button)

root.mainloop()