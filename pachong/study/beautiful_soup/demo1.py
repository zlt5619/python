"""
beautiful soup模块利用lxml解析xml文件
"""

from bs4 import BeautifulSoup

soup =BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)