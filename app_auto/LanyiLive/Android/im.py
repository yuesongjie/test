# coding=utf-8
from time import sleep
def zgjzd(driver):
    tabims = driver.find_elements_by_id('com.lanyi.live:id/iv_tab_icon')
    tabims[2].click()
    sleep(2)
    imtitle = driver.find_element_by_id('com.lanyi.live:id/text_title').get_attribute('name')
    if imtitle == u'与宁宁助理聊天中':
        print u'打开im成功'
    else:
        print u'打开im失败'
        pass
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
