# coding=utf-8
from appium import webdriver
from time import sleep
def qoute(driver):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="行情"]').click()
    sleep(2)
    driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
    sleep(2)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(int(x) / 2, int(y) * 2 / 3, int(x) / 2, 0, duration=sleep(3))
    driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
    sleep(1)
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="沪深"]').click()
    driver.swipe(int(x) / 2, int(y) * 2 / 3, int(x) / 2, 0, duration=sleep(3))
    driver.find_element_by_accessibility_id('换手率榜').click()
    driver.find_element_by_accessibility_id('search').click()
    sleep(3)
    driver.find_element_by_accessibility_id('backImg').click()
