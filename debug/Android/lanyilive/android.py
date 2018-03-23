# coding=utf-8
from appium import webdriver
from time import sleep
from homepage import home
from videolive import videoliving
from im import zgjzd
from quote import qoute
from personal import personalcenter
#appium Android配置
desired_caps={'deviceName': 'Z',
              'noReset': True,
              'platformVersion': '5.1.1',
              'appPackage': 'com.lanyi.live',
              'platformName': 'Android',
              'appActivity': '.business.launcher.SplashActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(3)
home(driver)
videoliving(driver)
zgjzd(driver)
qoute(driver)
personalcenter(driver)