# coding=utf-8
from time import sleep
def news(driver,x,y):
    driver.find_element_by_accessibility_id('资讯').click()
    driver.find_element_by_accessibility_id('期货学院').click()
    driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()
    sleep(2)
    driver.find_element_by_accessibility_id('back Icon').click()
    sleep(2)
    driver.find_element_by_accessibility_id('期货之声').click()
    albumarea = driver.find_element_by_xpath(
        '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    albumlist = albumarea.find_elements_by_class_name('XCUIElementTypeCell')
    for album in albumlist:
        print u'专辑名称: ' + album.find_elements_by_class_name('XCUIElementTypeStaticText')[0].get_attribute('name')
    sleep(3)
    driver.find_element_by_accessibility_id('期货资讯').click()
    driver.find_element_by_accessibility_id('期货要闻').click()
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    sleep(2)
    articlearea = driver.find_elements_by_class_name('XCUIElementTypeCell')[5]
    title = articlearea.find_elements_by_class_name('XCUIElementTypeStaticText')[0]
    title.click()
    sleep(2)
    driver.find_element_by_accessibility_id('back Icon').click()