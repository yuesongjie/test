#coding=utf-8
import requests
from bs4 import BeautifulSoup
url='https://soccer.hupu.com/china/'
headers={
'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
r=requests.get(url,headers=headers).content
soup=BeautifulSoup(r,'html.parser')
hp_wrap=soup.find('div',attrs={'class':'hp-wrap'})
soccer_sidebar=hp_wrap.find('div',attrs={'class':'soccer-sidebar'})
jfbarea=soccer_sidebar.find('div',attrs={'class':'soccer-box-B standings'})
tabscon=jfbarea.find('div',attrs={'class':'tabsCon'})
bd=tabscon.find('div')
soccer_table_A=bd.find('table')
tbody=soccer_table_A.find('tbody')
tr=tbody.find_all('tr')
for i in range(1,17):
    qd=tr[i].find('td',attrs={'class':"num2"}).get_text()
    win=tr[i].find('td',attrs={'class':"num3"}).get_text()
    draw=tr[i].find('td',attrs={'class':"num4"}).get_text()
    lose=tr[i].find('td',attrs={'class':"num5"}).get_text()
    score=tr[i].find('td',attrs={'class':"num6"}).get_text()
    print i,qd,win,draw,lose,score


