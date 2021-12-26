from urllib.request import urlopen,Request
from urllib.parse import urlencode
# url='https://www.baidu.com/s?wd=%E5%B0%9A%E5%AD%A6%E5%A0%82&ie=utf-8&tn=02003390_54_hao_pg'

args=input('请输入要搜索的内容')
parms={
    'wd':args,
    'ie':'utf-8'
}
url=f'https://www.baidu.com/s?{urlencode(parms)}'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

req=Request(url,headers=headers)

resp=urlopen(req)

print(resp.read().decode())