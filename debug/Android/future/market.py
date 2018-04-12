# coding=utf-8
from time import sleep
def market(driver):
    driver.find_element_by_id('com.lanyife.futures:id/navigation_market').click()
    sleep(2)
    driver.find_element_by_id('com.lanyife.futures:id/btnMarket').click()
    exchanges = driver.find_elements_by_id('com.lanyife.futures:id/tabs')
    exchangesarea = exchanges[0].find_element_by_class_name('android.widget.LinearLayout')
    exchangesarea.find_elements_by_class_name('android.widget.TextView')[1].click()
    varieties = exchanges[1].find_element_by_class_name('android.widget.LinearLayout')
    varieties.find_elements_by_class_name('android.widget.TextView')[4].click()
    sleep(1)
    contractlists = driver.find_element_by_id('com.lanyife.futures:id/listview')
    contractlists.find_elements_by_class_name('android.widget.RelativeLayout')[0].click()
    sleep(3)
    newprice = driver.find_element_by_id('com.lanyife.futures:id/text_price_new').get_attribute('name')
    if newprice == '--':
        print u'获取行情信息失败'
    else:
        print driver.find_element_by_id('com.lanyife.futures:id/title').get_attribute('name') + ':  ' + newprice
    driver.find_element_by_id('com.lanyife.futures:id/btn_contract').click()
    sleep(1)
    driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
    sleep(1)
    driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
    driver.find_element_by_id('com.lanyife.futures:id/btnSearch').click()
    sleep(1)
    driver.find_element_by_id('com.lanyife.futures:id/cancel_btn').click()

