# coding=utf-8
from time import sleep
def market(driver):
    driver.find_element_by_id('com.lanyife.futures:id/navigation_market').click()
    sleep(2)
    a=driver.find_element_by_id('com.lanyife.futures:id/swipeMenuListView')
    b=a.find_elements_by_class_name('android.widget.FrameLayout')[0]
    c=b.find_element_by_class_name('android.widget.LinearLayout')
    d=c.find_element_by_class_name('android.widget.LinearLayout')
    e=d.find_element_by_class_name('android.widget.LinearLayout')
    f=e.find_element_by_class_name('android.widget.RelativeLayout')
    f.click()
    sleep(2)
    driver.find_element_by_id('com.lanyife.futures:id/open_account_btn').click()
    driver.find_element_by_id('com.lanyife.futures:id/buy_state_tv').click()
    driver.find_elements_by_class_name('android.widget.TextView')[18].click()
    #交易
    moneycanuse=driver.find_element_by_id('com.lanyife.futures:id/can_use_count_tv').get_attribute('name')
    tradestatus=driver.find_element_by_id('com.lanyife.futures:id/state_tv').get_attribute('name')
    if tradestatus == u'交易中':
        print u'交易时间'
        newprice1 = driver.find_element_by_id('com.lanyife.futures:id/price_edit').get_attribute('name')
        if int(float(moneycanuse)) > 100000:
            print u'可用资金充足'
            if 23000 < int((float(newprice1))) < 25000:
                print u'价格合适操作'
                driver.find_element_by_id('com.lanyife.futures:id/count_edit').click()
                driver.find_element_by_id('com.lanyife.futures:id/delete_btn').click()
                driver.find_element_by_id('com.lanyife.futures:id/closed_iv').click()
                driver.find_element_by_id('com.lanyife.futures:id/confirm_btn').click()
                driver.find_element_by_id('com.lanyife.futures:id/confirm_btn').click()
            else:
                print u'价格不合适 不再操作'
        else:
            print u'可用资金不足'
    else:
        print u'非交易时间'
    driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
    driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
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

