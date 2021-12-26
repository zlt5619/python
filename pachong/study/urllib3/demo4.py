import urllib3

proxy=urllib3.ProxyManager('http://118.123.43.207:8080')
res=proxy.request('GET','http://httpbin.org/ip')
print(res.data)
