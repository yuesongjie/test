#coding=utf-8
from appium import webdriver
from time import sleep
desired_caps={}
desired_caps['platformName']='iOS'
desired_caps['platformVersion']='10.3'
desired_caps['deviceName']='iPhone 6s Plus'
desired_caps["noReset"]=True
desired_caps["udid"]=""
#desired_caps['udid']=''
desired_caps["xcodeOrgId"]="N8Y36ZQX9J"
desired_caps["xcodeSigningId"]="iOS Developer"
desired_caps["bundleId"]="com.tencent.xin"
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.find_element_by_accessibility_id(u'').click()
sleep(1)
driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="微信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[3]/XCUIElementTypeTextView').send_keys(u'Adobe')
sleep(1)
driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="微信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[3]/XCUIElementTypeTextView').send_keys('\n')
