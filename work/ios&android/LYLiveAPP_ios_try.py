#coding=utf-8
from appium import webdriver
from time import sleep
import random
import unittest
#配置
desired_caps={#'deviceName': 'iPhone 6s Plus',
                'deviceName': 'iPhone 6s',
              'xcodeOrgId': 'N8Y36ZQX9J',
              #'udid': '6eaec690714d9d23c386339e0c07268109d9fabc',
              'noReset': True,
              'xcodeSigningId': 'iOS Developer',
              'platformVersion': '10.3',
              'platformName': 'iOS',
              'bundleId': 'com.lanyizhibo.live'}
driver=webdriver.Remote('http://localhost:2333/wd/hub',desired_caps)
#个人中心
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="个人中心"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="立即登录"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="可使用手机号登录"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="股市e览"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField').send_keys('17301692962')
# sleep(1)
# driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="股市e览"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField').send_keys('ysj1025')
# sleep(1)
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="登录"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="股市e览"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
# sleep(1)
# driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="股市e览"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
# sleep(1)
# driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="股市e览"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
# sleep(1)
# driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="股市e览"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
#名师看盘
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="名师看盘"]').click()
driver.tap([(189,301)])
driver.swipe(159,474,31,-265,1000)
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
driver.swipe(182,540,28,-371,1000)
driver.swipe(182,540,28,-371,1000)
driver.swipe(182,540,28,-371,1000)
#诊股加战队
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="诊股/加战队"]').click()
sleep(3)
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
#视频解盘
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="视频解盘"]').click()
sleep(5)
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="互动"]').click()
sleep(2)
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="video full back"]').click()
#首页
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="首页"]').click()
sleep(1)
driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="名师看盘"]').click()
sleep(1)
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
sleep(2)
driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="视频解盘"]').click()
sleep(3)
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="video full back"]').click()
# driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="更多>>"])[1]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="卖出"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
# sleep(1)
# driver.swipe(156,595,172,186,1000)
# driver.swipe(156,595,172,186,1000)
# driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="王老师"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="backImg"]').click()
# #退出
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="个人中心"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeImage[@name="rigghtArrow"]').click()
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="退出登录"]').click()
driver.close_app()
