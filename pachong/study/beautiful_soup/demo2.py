html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacsie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/title" class="sister" id="link3">Tillite</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

#prettify把要解析的字符串以标准的缩进格式输出
print(soup.prettify())
print(soup.title.string)
