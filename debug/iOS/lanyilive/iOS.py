# coding=utf-8
from appium import webdriver
from time import sleep
from homepage import home
from videolive import live
from qoute import qoute
desired_caps={'platformName': 'iOS',
              'noReset': True,
              'platformVersion': '10.3',
              "deviceName": "iPhone 6s Plus",
              "bundleId": "com.lanyizhibo.live",
              "udid": "6eaec690714d9d23c386339e0c07268109d9fabc",
              "automationName":"XCUITest"}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(2)
try:
    home(driver)
    qoute(driver)
    live(driver)
except:
    print u'异常'
finally:
    driver.quit()

