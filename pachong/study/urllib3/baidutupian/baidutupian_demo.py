import urllib3
import re
'''
下载百度图片首页面的所有图片
'''
# 1.找到目标数据
page_url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1638241919441_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDYsMSw0LDIsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E7%8C%AB'
# 构造请求头，防止请求被禁止
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
# 2.分析请流程
# 下载html
http = urllib3.PoolManager()
res = http.request('get',page_url,headers=headers)
print(res.data.decode())
html = res.data.decode('utf-8')#通过ctrl+f查找charset
# 提取img_urls
img_urls = re.findall(r'"thumbURL":"(.*?)"',html)
# print(img_urls)


# 遍历 下载
for index,img_url in enumerate(img_urls):
    # 下载图片
    img_res = http.request('get',img_url,headers=headers)
    # 动态的拼接文件名
    img_file_name = '%s.%s'%(index,img_url.split('.')[-1])
    with open('img_file_name','wb') as f:
        f.write(img_res.data)
