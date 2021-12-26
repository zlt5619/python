import urllib3

http = urllib3.PoolManager()
# r = http.request('GET','http://www.baidu.com')
# r=http.request('GET','http://httpbin.org/ip')
r=http.request('GET','https://www.csdn.net/')
print(r.status)
print(r.data)
print(r.headers)