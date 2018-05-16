# coding=utf-8
from time import sleep
def trade(driver):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="模拟交易"]').click()
    sleep(3)
    driver.find_element_by_accessibility_id('资金详情').click()
    sleep(1)
    driver.find_element_by_accessibility_id('back Icon').click()
    currentfund = driver.find_elements_by_class_name('XCUIElementTypeStaticText')[4].get_attribute('value')
    print u'当前权益： ' + currentfund
    nousemoney = driver.find_elements_by_class_name('XCUIElementTypeStaticText')[7].get_attribute('value')
    print u'可用资金： ' + nousemoney
    print u'保证金： ' + str(float(currentfund) - float(nousemoney))
    driver.find_element_by_accessibility_id('我的比赛').click()
    print u'参加的比赛： ' + driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="期冠谁手"]').get_attribute('name')
    driver.find_element_by_accessibility_id('back Icon').click()
    driver.find_element_by_accessibility_id('当前挂单').click()
    driver.find_element_by_accessibility_id('全部委托').click()
    driver.find_element_by_accessibility_id('成交').click()
    driver.find_element_by_accessibility_id('全部持仓').click()
    holdlist=driver.find_element_by_class_name('XCUIElementTypeTable')
    holdkind=holdlist.find_elements_by_class_name('XCUIElementTypeCell')
    holdnums=len(holdkind)
    count = 0
    if holdnums==1:
        holdkind = holdlist.find_element_by_class_name('XCUIElementTypeCell')
        hold=holdkind.find_elements_by_class_name('XCUIElementTypeStaticText')
        print u'持有' + hold[0].get_attribute('name')+ hold[5].get_attribute('name') + ',' + u'浮盈' + hold[7].get_attribute('name')
        count = count +(float(hold[7].get_attribute('name')))
    else:
        for holdkin in holdkind:
            hold=holdkin.find_elements_by_class_name('XCUIElementTypeStaticText')
            print u'持有'+hold[0].get_attribute('name')+' '+hold[6].get_attribute('name')+','+u'浮盈'+hold[7].get_attribute('name')
            count=count+float(hold[7].get_attribute('name'))
    print u'当前浮盈合计'+unicode(count)