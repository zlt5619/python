from urllib import request,parse
'''
urllib库
'''
url = 'http://httpbin.org/get?username={}'.format(parse.quote('五更灯火'))
print(url)
response = request.urlopen(url)
print(response.read().decode())
