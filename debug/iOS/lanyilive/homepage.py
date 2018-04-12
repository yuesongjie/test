# coding=utf-8
from time import sleep
def home(driver):
    sleep(2)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    try:
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="signIn deleteImage"]').click()
    except:
        print u'没有签到弹窗'
    try:
        driver.find_element_by_accessibility_id('notice close btn').click()
    except:
        print u'没有弹窗广告'
    finally:
        sleep(2)
    driver.find_element_by_accessibility_id('名师专栏').click()
    sleep(1)
    driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 600, duration=sleep(3))
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 600, duration=sleep(3))
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_accessibility_id('backImg').click()
    # driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="股票看板"]').click()
    # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="最近买入"]').click()
    # driver.find_element_by_xpath(
    #     '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
    # sleep(2)
    # try:
    #     driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="无数据"]')
    # except:
    #     pass
    # finally:
    #     driver.swipe(int(x) / 2, int(y) * 2 / 3, int(x) / 2, 0, duration=sleep(3))
    # driver.swipe(int(x) / 2, int(y) * 2 / 3, int(x) / 2, 0, duration=sleep(3))
    # driver.find_element_by_xpath(
    #     '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[3]').click()
    # sleep(1)
    # driver.find_element_by_accessibility_id('backImg').click()
    # driver.find_element_by_accessibility_id('backImg').click()
    # driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="视频回顾"]').click()
    sleep(2)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="playblack centerPlay"]').click()
    sleep(4)
    driver.find_element_by_xpath(
        '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther').click()
    driver.find_element_by_accessibility_id('video full back').click()
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="股市学院"]').click()
    sleep(2)
    driver.find_element_by_xpath('(//XCUIElementTypeLink[@name="基本分析"])[1]').click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="文章列表"]')
    except:
        print u'网络异常'
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('(//XCUIElementTypeLink[@name="技术分析"])[1]').click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="文章列表"]')
    except:
        print u'网络异常'
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('(//XCUIElementTypeLink[@name="实战技巧"])[1]').click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="文章列表"]')
    except:
        print u'网络异常'
    driver.find_element_by_accessibility_id('backImg').click()
    sleep(1)
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="股市内参"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="一分钟极速开户"]')
    except:
        print u'打开失败'
    driver.find_element_by_accessibility_id('backImg').click()
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 600, duration=sleep(3))
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 600, duration=sleep(3))
    # driver.swipe(int(x) / 2, int(y)/2, int(x) / 2, int(y) / 600, duration=sleep(3))
    textarea = driver.find_element_by_xpath(
        '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]')
    clickareas = textarea.find_elements_by_class_name('XCUIElementTypeStaticText')
    if len(clickareas) == 4:
        clickareas[2].click()
    else:
        textarea = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]')
        clickareas = textarea.find_elements_by_class_name('XCUIElementTypeStaticText')
        clickareas[2].click()
    sleep(3)
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="览益头条"])').click()
    driver.find_element_by_xpath(
        '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
    sleep(2)
    driver.find_element_by_accessibility_id('backImg').click()
    driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="市场快讯"])').click()
    sleep(1)
    driver.find_element_by_xpath(
        '//XCUIElementTypeApplication[@name="览益股市"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]').click()
    sleep(2)
    driver.find_element_by_accessibility_id('backImg').click()
