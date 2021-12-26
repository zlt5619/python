from urllib import request
from http import cookiejar

"""
1、创建一个cookie对象
2、创建一个cookie处理器
3、以它为参数，创建一个Openner对象
4、使用这个openner来发送请求pip
"""
cookie=cookiejar.CookieJar()
cookies=request.HTTPCookieProcessor(cookie)
openner=request.build_opener(cookies)
res=openner.open('http://www.baidu.com')

print(cookies.cookiejar)