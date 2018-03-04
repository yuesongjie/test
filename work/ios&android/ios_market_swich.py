#coding=utf-8
from appium import webdriver
from time import sleep
import random
#配置
desired_caps={#'deviceName': 'iPhone 6s Plus',
                'deviceName': 'iPhone 6s',
              'noReset': True,
              'xcodeSigningId': 'iOS Developer',
              'platformVersion': '10.3',
              'platformName': 'iOS',
              }
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
def enter_market():
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="行情"]').click()
    sleep(1)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="主力"]').click()
    driver.tap([(232, 104)])
    sleep(1)
def see_market():
    enter_market()
    a=driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1分"]')
    b=driver.find_element_by_xpath('//XCUIElementTypeButton[@name="5分"]')
    c=driver.find_element_by_xpath('//XCUIElementTypeButton[@name="15分"]')
    d=driver.find_element_by_xpath('//XCUIElementTypeButton[@name="30分"]')
    e=driver.find_element_by_xpath('//XCUIElementTypeButton[@name="60分"]')
    f=driver.find_element_by_xpath('//XCUIElementTypeButton[@name="日K"]')
    lists=[a,b,c,d,e,f]
    ks=random.sample(lists,4)
    for k in ks:
        k.click()
        sleep(2)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="back Icon"]').click()
while True:
    see_market()