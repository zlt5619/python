from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=[], excludes=[])
import sys
import os

os.environ['TCL_LIBRARY'] = 'I:\\Python37\\tcl\\tcl8.6'
os.environ['Tk_LIBRARY'] = 'I:\\Python37\\tcl\\tk8.6'
base = 'Win32GUI' if sys.platform == 'win32' else None
includes = []
includes_files = ['I:\\Python37\\DLLs\\tcl86t.dll',
                  'I:\\Python37\\DLLs\\tk86t.dll']  # 改成自己存放路径
executables = [
    Executable('I:\\Python36\\Scripts\\gui_local_baidu.py', base=base, targetName='convert_success.exe')
]  # gui_local_baidu.py需要改成自己的py文件

setup(name='convert_local',
      version='0.1',
      description='convert_baidu',
      # options = {"build_exe":{"includes":includes,"includes_files":includes_files}},
      executables=executables

      )
