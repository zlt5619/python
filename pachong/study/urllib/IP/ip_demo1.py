"""
好好掌握

"""

from urllib import request

url='http://httpbin.org/ip'

#代理地址
proxy={'http':'180.76.111.69:3128'}

# 代理服务器
proxies=request.ProxyHandler(proxy)

# 创建openner对象
openner=request.build_opener(proxies)

res=openner.open(url)

print(res.read().decose())