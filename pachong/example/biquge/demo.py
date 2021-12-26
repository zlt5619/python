from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

url='https://www.biquge7.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Cookie': ''
}


req=Request(url=url,headers=headers)
resp=urlopen(req)
html=resp.read().decode('utf-8','ignore')

soup = BeautifulSoup(html,'lxml')
div1=soup.find(attrs={'class':'hot'})
div_list=div1.find_all(attrs={'class':'item'})
zuozhe_list=[]
shuming_list=[]
for i in div_list:
    dt=i.find(name='dt')
    zuozhe_list.append(dt.find(name='span').string)
    shuming_list.append(dt.find(name='a').string)
print(zuozhe_list)
print(shuming_list)