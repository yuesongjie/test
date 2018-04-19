# coding=utf-8
from time import sleep
def home(driver,x,y):
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    articlearea = driver.find_element_by_class_name('XCUIElementTypeTable')
    article = articlearea.find_elements_by_class_name('XCUIElementTypeCell')[5]
    article.find_elements_by_class_name('XCUIElementTypeStaticText')[0].click()
    sleep(4)
    driver.find_element_by_accessibility_id('back Icon').click()
    sleep(1)

