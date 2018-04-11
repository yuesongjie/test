# coding=utf-8
from appium import webdriver
from time import sleep
def qoute(driver):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="行情"]').click()
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="沪深"]').click()
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(int(x) / 2, int(y) * 2 / 3, int(x) / 2, 0, duration=sleep(3))
    driver.find_element_by_accessibility_id('换手率榜').click()
    driver.find_element_by_accessibility_id('search').click()
    driver.find_element_by_accessibility_id('backImg').click()
