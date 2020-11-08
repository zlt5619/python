from pyautocad import Autocad, APoint
from get_class_info import get_all_info
acad = Autocad(create_if_not_exists = True)



print(dir(acad.ActiveDocument))
print(type(acad.ActiveDocument))
print(acad.ActiveDocument.__dict__)

# print(acad.ActiveDocument.Blocks.Add.__code__.co_argcount)
# print(acad.ActiveDocument.Blocks.Add.__code__.co_varnames)

# print(dir(acad.model))
# print(type(acad.model))
# print(acad.model.__dict__)
#
# print(type(acad.prompt))
