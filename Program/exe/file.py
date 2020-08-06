"""
如下所示为python3.6的32位，需要下载[pywin32-223.win32-py3.6.exe]
Python 3.6.3 ... [MSC v.1900 32 bit (Intel)] on win32
如下所示为python3.6的64位，需要下载[pywin32-223.win-amd64-py3.6.exe]
Python 3.6.3 ... [MSC v.1900 64 bit (AMD64)] on win32
3.在命令行中直接输入下面的指令即可
pyinstaller [opts] yourprogram.py
参数含义

-F 指定打包后只生成一个exe格式的文件(建议写上这个参数)

-D –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）

-c –console, –nowindowed 使用控制台，无界面(默认)

-w –windowed, –noconsole 使用窗口，无控制台

-p 添加搜索路径，让其找到对应的库。

-i 改变生成程序的icon图标(比如给女朋友写的程序，换个好看的图标，默认的很丑)

实例说明
比如你有个python程序叫test.py，绝对路径在[D:\project]，打包成一个exe格式的文件
pyinstaller -F D:\project\test.py
条件同上，如果还希望没有控制台的黑框框，在进程中偷偷运行
pyinstaller -F -w D:\project\test.py
条件同上，如果还希望更换程序图标
pyinstaller -F -w -i D:\project\test.ico D:\project\test.py
结果展示

在你的py文件所在的目录下，生成build和dist文件夹，如果是选择了-F参数，那么dist文件夹下就是你要的程序，build文件夹可以删除

注意，pyinstaller只能在windows电脑环境下进行转换。同时建议路径使用英文，不要包含中文，低版本的pyinstaller可能会出错。


"""