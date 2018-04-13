# coding=utf-8
from appium import webdriver
from time import sleep
desired_caps={'deviceName': 'Z',
              'noReset': True,
              'platformVersion': '5.1.1',
              'appPackage': "com.lanyife.futures",
              'platformName': 'Android',
              'appActivity': '.mvp.ui.activity.WelcomeActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
sleep(5)
driver.find_element_by_id('com.lanyife.futures:id/navigation_all').click()
sleep(3)
currentfund=driver.find_element_by_id('com.lanyife.futures:id/current_fund_tv').get_attribute('name')
moneycanbeused=driver.find_element_by_id('com.lanyife.futures:id/can_use_fount_tv').get_attribute('name')
print u'当前总权益"'+' '+currentfund+','+u'可用资金:'+' '+moneycanbeused
driver.find_element_by_id('com.lanyife.futures:id/fund_detail_btn').click()
currentfund_d=driver.find_element_by_id('com.lanyife.futures:id/current_fund_tv').get_attribute('name')
if currentfund_d==currentfund:
    pass
else:
    print u'网络异常'
driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
driver.find_element_by_id('com.lanyife.futures:id/competition_btn').click()
matchname=driver.find_element_by_id('com.lanyife.futures:id/title').get_attribute('name')
if matchname !=' ':
    print matchname
else:
    print u'网络异常'
driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
operatebar0=driver.find_element_by_id('com.lanyife.futures:id/id_stickynavlayout_indicator')
operatebar1=operatebar0.find_element_by_class_name('android.widget.LinearLayout')
operatebar2=operatebar1.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
currenthang=operatebar2[1].click()
currentdelegate=operatebar2[2].click()
deal=operatebar2[3].click()
driver.find_element_by_id('com.lanyife.futures:id/trade_btn').click()
sleep(1)
driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
operatebar2[0].click()