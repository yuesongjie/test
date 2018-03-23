# coding=utf-8
from time import sleep
def qoute(driver):
    qoutetabs=driver.find_elements_by_id('com.lanyi.live:id/iv_tab_icon')
    qoutetabs[3].click()
    sleep(5)
    currentprices=driver.find_elements_by_id('com.lanyi.live:id/text_current')
    currentprice=currentprices[1].get_attribute('name')
    if currentprice=='--':
        print u'自选行情加载失败'
    else:
        print u'加载自选行情成功'
    hushentabs=driver.find_elements_by_id('com.lanyi.live:id/tv_tab_title')
    for hushentab in hushentabs:
        tabnames=hushentab.get_attribute('name')
        if tabnames==u'沪深':
           hushentab.click()
        else:
            pass
    try:
        driver.find_elements_by_id('com.lanyi.live:id/text_price')
    except:
        print u'行情加载失败'
        driver.quit()
    driver.find_elements_by_id('com.lanyi.live:id/text_name')[1].click()
    sleep(1)
    driver.find_elements_by_id('com.lanyi.live:id/text_current')[1].click()
    sleep(1)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(3))
    driver.find_elements_by_id('com.lanyi.live:id/text_title')[3].click()
    sleep(1)
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(3))
    driver.find_elements_by_id('com.lanyi.live:id/text_title')[0].click()
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(3))
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.find_element_by_id('com.lanyi.live:id/btn_search').click()
    sleep(1)
    driver.find_element_by_id('com.lanyi.live:id/view_edit').send_keys('600000')
    driver.find_element_by_id('com.lanyi.live:id/text_stock').click()
    sleep(2)
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    print u'查看行情部分成功'