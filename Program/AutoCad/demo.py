from pyautocad import Autocad

# 自动连接上cad，只要cad是开着的，就创建了一个<pyautocad.api.aautocad> 对象。这个对象连接最近打开的cad文件。
# 如果此时还没有打开cad，将会创建一个新的dwg文件，并自动开启cad软件
acad = Autocad(create_if_not_exists=True)
# acad.prompt() 用来在cad控制台中打印文字
acad.prompt("Hello, aautocad from Python")
# acad.doc.Name储存着cad最近打开的图形名
print(acad.doc.Name)

