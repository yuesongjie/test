#coding=utf-8
from selenium import webdriver
from time import sleep
import sys
import time
import datetime
from selenium.webdriver.common.keys import Keys
import codecs
from bs4 import BeautifulSoup
from openpyxl import Workbook
URL='http://train.qunar.com/'
def ordertickert(driver,from_city,to_city):
    driver.find_element_by_name('fromStation').clear()
    driver.find_element_by_name('fromStation').send_keys(from_city)
    driver.find_element_by_name('fromStation').send_keys(Keys.ENTER)
    sleep(2)
    driver.find_element_by_name('toStation').clear()
    driver.find_element_by_name('toStation').send_keys(to_city)
    driver.find_element_by_name('toStation').send_keys(Keys.ENTER)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="js-con"]/div[1]/form/div[2]/div/span/button').click()
    sleep(5)
    source_code = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    f=codecs.open('result'+ u'.html', 'w+', 'utf8')
    f.write(source_code)
    f.close()
    print u'存储完成'
def search():
    from_city = raw_input(u'请输入您的出发地：').decode(sys.stdin.encoding)
    to_city = raw_input(u'请输入您的目的地：').decode(sys.stdin.encoding)
    driver=webdriver.Firefox()
    driver.get(URL)
    sleep(2)
    ordertickert(driver, from_city, to_city)
    driver.close()
def createxcel():
    wb = Workbook()  # 新建excel
    dest_filename ='result.xlsx'  # 设定文件名
    ws1 = wb.active  # 激活
    ws1.title = u'结果'
    ws1['A1'] = u'车次'
    ws1['C1'] = u'发车时间'
    ws1['B1'] = u'到达站'
    ws1['E1'] = u'到达时间'
    ws1['D1'] = u'到达站'
    ws1['F1'] = u'时长'
    ws1['G1'] = u"注：'+1'代表次日到达"
    files = open(r'result.html', 'r')
    filepage = files.read()
    tnum = []
    from_station = []
    to_station = []
    from_time = []
    to_time = []
    during = []
    soup = BeautifulSoup(filepage, 'html.parser')
    ul = soup.find('ul', class_='tbody')
    for i in ul.find_all('li'):
        listinfo = i.find('div', attrs={'class': 'js_listinfo'})
        td1 = listinfo.find('div', attrs={'class': 'td col1 js-trainNum'})
        h3 = td1.find('h3', attrs={'class': 'train'})
        tnums = h3.get_text().strip()  # 车次
        tnum.append(tnums)
        td2 = listinfo.find('div', attrs={'class': 'td col2'})
        start = td2.find('p', attrs={'class': 'start'})
        from_stations = start.find('span').get_text().strip()
        from_station.append(from_stations)
        to = td2.find('p', attrs={'class': 'end'})
        to_stations = to.find('span').get_text()
        to_station.append(to_stations)  # 乘/到站
        td22 = listinfo.find_all('div', attrs={'class': 'td col2'})
        startime = td22[1]
        from_times = startime.find('time').string
        from_time.append(from_times)
        from_time1 = startime.find_all('time')
        to_times = from_time1[1].get_text()
        to_time.append(to_times)
        td6 = listinfo.find('div', attrs={'class': 'td col6'})
        duringtime = td6.find('time')
        durings = duringtime.string
        during.append(durings)
    for (i, m, o, p, t, q) in zip(tnum, from_time, to_time, from_station, to_station, during):
        col_A = 'A%s' % (tnum.index(i) + 2)
        col_B = 'B%s' % (tnum.index(i) + 2)
        col_C = 'C%s' % (tnum.index(i) + 2)
        col_D = 'D%s' % (tnum.index(i) + 2)
        col_E = 'E%s' % (tnum.index(i) + 2)
        col_F = 'F%s' % (tnum.index(i) + 2)
        ws1[col_A] = i
        ws1[col_B] = p
        ws1[col_C] = m
        ws1[col_D] = t
        ws1[col_E] = o
        ws1[col_F] = q
        wb.save(filename=dest_filename)
if __name__ == '__main__':
    print u"开始"
    start = datetime.datetime.now()
    search()
    createxcel()
    end = datetime.datetime.now()
    print u"结束"
    print u"完成时间: ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
