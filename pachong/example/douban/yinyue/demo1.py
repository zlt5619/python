"""
获取豆瓣音乐排名的作品和歌手
"""

from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

url='https://music.douban.com/chart'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
req=Request(url=url,headers=headers)
resp=urlopen(req)

html=resp.read().decode()
soup = BeautifulSoup(html,'lxml')
# gequ_list=soup.find_all(attrs={'href':'javascript:;'})
# # for i in gequ_list:
# #     print(i.string)
# zuoqu_list=soup.find_all(attrs={'class':'intro'})
# for i in zuoqu_list:
#     print(i.find(name='p'))
# # print(type(soup.find_all(attrs={'class':'col5'})))

"""
先找到整体的ul
再找到全部的li

"""
gequ_list=[]
geshou_list=[]
ul=soup.find(attrs={'class':'col5'})
li_list=ul.find_all(name='li')
for i in li_list:
    gequ_list.append(i.find(attrs={'href':'javascript:;'}).string)
    if i.find(name='p').string==None:
        list1=i.find(name='p').text.split('\n')
        geshou_list.append(list1[2].split('/')[0].lstrip().split('\xa0')[0])


    else:
        geshou_list.append(i.find(name='p').string.split('\xa0')[0])

print(gequ_list)
print(geshou_list)




