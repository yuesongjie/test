#coding=utf-8
import requests
from appium import webdriver
import time
#获取行情信息
url='http://webftcn.hermes.hexun.com/shf/quotelist?code=SHFE3ZN1803&column=Price,BuyPrice,Sellprice'
#手机配置
desired_caps={
                'deviceName': 'iPhone 6s Plus',
                # 'deviceName': 'iPhone 6',
              #'xcodeOrgId': 'N8Y36ZQX9J',
              # 'udid':'47efdde692f91692072e31168f6ffc022ffbe407',
              'udid': '6eaec690714d9d23c386339e0c07268109d9fabc',
              'noReset': True,
              'xcodeSigningId': 'iOS Developer',
              'platformVersion': '10.3',
              'platformName': 'iOS',
              'bundleId': 'com.lanyilive.YXFuture'}
while True:
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    while True:
        r1 = requests.get(url).content
        nowprice = int(r1[12:17])#这货返回的是字符串
        buyprice = int(r1[19:24])
        buypricefinal=buyprice-10
        sellprice = int(r1[35:40])
        print 'buyprice: '+str(buyprice),',','final buyprice: '+str(buypricefinal)
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="行情"]').click()
        # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="自选"]').click()
        allarea = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable')
        firstone = allarea.find_elements_by_class_name('XCUIElementTypeCell')[0]
        firstone.click()
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="模拟交易"]').click()
        time.sleep(2)
        tapbar = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther')
        tags = tapbar.find_elements_by_class_name('XCUIElementTypeButton')
        tags[0].click()  # 0:多,2:空,3:持仓
        pricearea = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]')
        pricearea.click()
        keyboardarea = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]')
        num1 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]')
        num2 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]')
        num3 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="3"]')
        num4 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="4"]')
        num5 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="5"]')
        num6 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="6"]')
        num7 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="7"]')
        num8 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="8"]')
        num9 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="9"]')
        num0 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="0"]')
        numspot = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="."]')
        numclear = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="mock keyboard delete"]')
        inptcomplete = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="mock keyboard finish"]')
        buypricestr = str(buypricefinal)
        pricelist = list(buypricestr)
        for price in pricelist:
            if price == '1':
                num1.click()
            elif price == '2':
                num2.click()
            elif price == '3':
                num3.click()
            elif price == '4':
                num4.click()
            elif price == '5':
                num5.click()
            elif price == '6':
                num6.click()
            elif price == '7':
                num7.click()
            elif price == '8':
                num8.click()
            elif price == '9':
                num9.click()
            elif price == '0':
                num0.click()
            elif price == '.':
                numspot.click()
            else:
                pass
        inptcomplete.click()
        handsarea = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]')
        handsarea.click()
        keyboardarea2 = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')
        cancel = keyboardarea2.find_element_by_xpath('//XCUIElementTypeButton[@name="mock keyboard finish"]')
        cancel.click()
        numberset = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1/2"]')
        numberset.click()
        # settingarea
        sa = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther')
        BUTTON = sa.find_element_by_class_name('XCUIElementTypeButton')
        print 'pass'
        try:
            BUTTON.click()
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="确定"]').click()
            print 'click done'
            time.sleep(3)
        except:
            print 'fail'
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="back Icon"]').click()
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="back Icon"]').click()
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="模拟交易"]').click()
        imgarea = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]')
        ratearea=imgarea.find_element_by_class_name('XCUIElementTypeOther')
        print ratearea
        rate = ratearea.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        print rate
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="当前挂单"]').click()
        hangorder = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="期货狙击手"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTable')
        hangnum = len(hangorder.find_elements_by_class_name('XCUIElementTypeCell'))
        print hangnum
        if hangnum > 3:
            driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="撤单"])[1]').click()
            driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="撤单"])[2]').click()
        else:
            pass
        break
