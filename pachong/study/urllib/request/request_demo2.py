from urllib import request
'''
urllib库
'''
# 设置超时
# request.urlopen("http://httpbin.org/get",timeout=0.1)

# 发送一个get请求
response = request.urlopen(url="http://httpbin.org/get")

# 发送一个post请求
response2 = request.urlopen(
    url="http://httpbin.org/post",
    data = b'username=wgdh&password=123456'
)

print(response.getcode())
print(response2.getcode())
