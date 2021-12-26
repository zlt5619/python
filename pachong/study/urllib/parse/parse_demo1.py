from urllib import parse

url = 'http://httpbin/org/get?aaa={}'
safe_url = url.format(parse.quote('五更灯火'))
print(safe_url)