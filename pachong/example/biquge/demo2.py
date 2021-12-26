from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

url='https://www.biquge7.com/book/1031/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Cookie': ''
}

req=Request(url=url,headers=headers)
resp=urlopen(req)
html=resp.read().decode('utf-8','ignore')

soup = BeautifulSoup(html,'lxml')
zhengti_div=soup.find(attrs={'class':'listmain'})
dd_list=zhengti_div.find_all(name='dd')
url_list=[]
for dd in dd_list:
    str1=dd.find(name='a')['href']
    if '/' not in str1:
        pass
    else:
        list1=str1.split('/')
        url_list.append(url+list1[-1])
# print(url_list)
f_path = r'C:/Users/zlt/Desktop/demo.txt'
txt_list=""
for i in url_list:
    req=Request(url=i,headers=headers)
    resp=urlopen(req)
    html = resp.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'lxml')
    txt = soup.find(attrs={'id': 'chaptercontent'}).text
    txt_list+=txt
with open(f_path,'wb') as f:
    f.write(bytes(txt_list,encoding='utf-8'))




# req=Request(url=url_list[0],headers=headers)
# resp=urlopen(req)
# html=resp.read().decode('utf-8', 'ignore')
# soup = BeautifulSoup(html,'lxml')
# txt=soup.find(attrs={'id':'chaptercontent'})
# print(txt.text)