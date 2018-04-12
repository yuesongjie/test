# coding=utf-8
from appium import webdriver
from time import sleep
def home(driver,x,y):
    sleep(2)
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    driver.find_elements_by_id('com.lanyife.futures:id/title')[1].click()
    sleep(2)
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    sleep(1)
    driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()