"""
读取excel表格
"""
import openpyxl
from openpyxl import Workbook,load_workbook
from openpyxl.styles import *
import warnings
warnings.filterwarnings('ignore')
path="C:/Users/zlt/Desktop/刘梦/曲线图制作/附件1：大幕山风电场24号机组发电机温度数据.xls"
wb = load_workbook(path)
print(wb)