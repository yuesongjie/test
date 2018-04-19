# coding=utf-8
from appium import webdriver
from time import sleep
from homepage import home
from market import market
from trade import trade
from news import news
desired_caps={'platformName': 'iOS',
              'noReset': True,
              'platformVersion': '10.3',
              "deviceName": "iPhone 6s Plus",
              "bundleId": "com.lanyilive.YXFuture",
              "udid": "6eaec690714d9d23c386339e0c07268109d9fabc",
              "automationName":"XCUITest"}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(2)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
home(driver,x,y)
market(driver)
trade(driver)
news(driver,x,y)