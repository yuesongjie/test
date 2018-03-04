#coding=utf-8
from selenium import webdriver
from time import sleep
import sys
import time
import datetime
from selenium.webdriver.common.keys import Keys
import codecs
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
    sleep(3)
    driver.maximize_window()
    sleep(2)
    ordertickert(driver, from_city, to_city)
    driver.close()
if __name__ == '__main__':
    print u"开始"
    start = datetime.datetime.now()
    search()
    end = datetime.datetime.now()
    print u"结束"
    print u"完成时间: ",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))