import tkinter as tk
root = tk.Tk()
from tkinter.filedialog import askopenfilename,askopenfilenames,askdirectory,asksaveasfilename

#这个对话框，可以让用户选择一个文件,选择一个文件，返回此文件路径的字符串，如果不选择，Cancel或直接关闭，返回一个空的字符串
#可以选择的参数title，initialdir，filetypes
#askopenfilename(title='Please choose a file',
#                  initialdir='/', filetypes=[('Python source file','*.py')])
# path=askopenfilename()
# print(path)

#同上面的用法，可以选择多个文件，返回tuple
# path=askopenfilenames()
# print(type(path))
# print(path)

#选择文件夹
# path=askdirectory()
# print(path)

#让用户指定一个文件保存数据。
asksaveasfilename()