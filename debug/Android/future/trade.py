# coding=utf-8
from appium import webdriver
from time import sleep
desired_caps={'deviceName': 'Z',
              'noReset': True,
              'platformVersion': '5.1.1',
              'appPackage': "com.lanyife.futures",
              'platformName': 'Android',
              'appActivity': '.mvp.ui.activity.WelcomeActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
sleep(2)
driver.find_element_by_id('com.lanyife.futures:id/navigation_all').click()