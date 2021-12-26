from urllib.request import Request,urlopen

url='http://www.baidu.com'

req=Request(url=url)

resp=urlopen(req)

print(resp.read().decode())