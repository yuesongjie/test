#coding=utf-8
import requests
from bs4 import BeautifulSoup
url='http://www.qihuo18.com/'
headers={
'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
r=requests.get(url,headers=headers).content
soup=BeautifulSoup(r,'html.parser')
content_big=soup.find('div',attrs={'class':'contentContainer contentContainer--withRight u-marginTop20'})
content_main=content_big.find('div',attrs={'class':'contentMain contentMain--withSide '})
contentMain=content_main.find('div',attrs={'class':'contentMain__content'})
hotspot_area=contentMain.find('div',attrs={'class':'hotspot u-marginTop20'})
hotspot_title=hotspot_area.find('div',attrs={'class':'hotspot__label'}).get_text()
hotspotList=hotspot_area.find('div',attrs={'class':'hotspotList'})
hotspots=hotspotList.find_all('div',attrs={'class':'news news--zx'})
for hotspot in hotspots:
    news=hotspot.find('div',attrs={'class':'news__contentWp u-nbfc'})
    news_part=news.find('h2',attrs={'class':'news__title'})
    news_title=news_part.find('a').get_text()
    title=news_title
    print news_title