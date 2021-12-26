from urllib.request import urlopen

response=urlopen("http://www.baidu.com/")

# print(response.read().decode())
# print(response.read())
# print(response.getcode())       #获取状态码，正常返回200，也会返回404，403，判断如何处理相应数据
# print(response.geturl())
print(response.info())      #返回响应头