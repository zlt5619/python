from urllib import request
'''
urllib库
headers
'''
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    #如果请求遇到403 Forbidden 一般使用Referer可以解决
    'Referer':'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87'
}
req = request.Request(
    url='https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2F711%2F101913115130%2F131019115130-5-1200.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1640829321&t=41a84305fe4a6d883b9714ac6eb8e52f',
    headers=headers
)

response = request.urlopen(req)
#将访问到的文件，写成jpg格式
with open('demo3_test.jpg','wb') as f:
    f.write(response.read())
