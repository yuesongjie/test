# coding=utf-8
from appium import webdriver
from time import sleep
def live(driver):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="视频解盘"]').click()
    sleep(3)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="互动"]').click()
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="请输入您的评论"]').send_keys(u'谢谢老师')
    sleep(2)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="发送"]').click()
    sleep(2)

