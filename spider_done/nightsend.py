#coding=utf-8
import requests
import time
url='http://webftcn.hermes.hexun.com/shf/quotelist?code=SHFE3CU1805&column=Price,BuyPrice,Sellprice'
while True:
    r1 = requests.get(url).content
    price = int(r1[12:17])#这货返回的是字符串
    buyprice=int(r1[19:24])
    sellprice=int(r1[35:40])
    url1='http://www-test.qihuo18.cn/api/v1/trade/user'
    url2='http://www-test.qihuo18.cn/api/v1/trade/putorder'
    # para={
    # 'symbol':'CU1805.XSGE',
    # 'price':buyprice,
    # 'num':1,
    # 'todayfirst':0,
    # 'type':1,
    # }
    # headers={
    # 'TOKEN':'V2_7ea9a5824fcc4160ced22f8a52c79bbd',
    # 'PL':'IOS',
    # 'APPVER':'2.0.0'
    # }
    # gettime = requests.post(url=url1,headers=headers)
    # # print gettime.content
    # sendreq=requests.post(url=url2,data=para,headers=headers)
    # scont=sendreq.content
    # servertime=scont[57:70]
    # print servertime
    break
flotime=time.time()
milis=int(round(flotime*1000))
print milis


