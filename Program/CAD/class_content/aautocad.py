from pyautocad import Autocad

# 自动连接上cad，只要cad是开着的，就创建了一个<pyautocad.api.aautocad> 对象。这个对象连接最近打开的cad文件。
# 如果此时还没有打开cad，将会创建一个新的dwg文件，并自动开启cad软件
acad = Autocad(create_if_not_exists=True)

for a in dir(acad):
    print(a)

"""
ActiveDocument
Application
__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__


__weakref__
_app
_create_if_not_exists
_visible


aDouble
aInt
aShort
app
best_interface
doc
find_one
get_selection
iter_layouts
iter_objects
iter_objects_fast
model
prompt
"""