# coding=utf-8
from time import sleep
def market(driver):
    sleep(1)
    driver.find_element_by_accessibility_id('行情').click()
    driver.find_element_by_accessibility_id('沪锌1806').click()
    sleep(1)
    driver.find_element_by_accessibility_id('模拟交易').click()
    try:
        driver.find_element_by_accessibility_id('非交易时间')
    except:
        print u'当前为交易时间'
        try:
            driver.find_element_by_accessibility_id('加多').click()
            driver.find_element_by_accessibility_id('最新价').click()
            currentpricefield = driver.find_elements_by_class_name('XCUIElementTypeTextField')
            currentpricecom = currentpricefield[0].get_attribute('value')
            price = int(currentpricecom[0:5])
            print u'最新价： ' + str(price)
            if 23050 < price < 25000:
                currentpricefield[0].click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                currentpricefield[1].click()
                driver.find_element_by_accessibility_id('mock keyboard delete').click()
                sleep(1)
                driver.find_element_by_accessibility_id('mock keyboard finish').click()
                nums = currentpricefield[1].get_attribute('value')
                print u'手数： ' + nums
                driver.find_element_by_accessibility_id('确认加多').click()
                driver.find_element_by_accessibility_id('确定').click()
                sleep(1)
                driver.find_element_by_accessibility_id('止盈/止损').click()
                sleep(3)
                driver.find_element_by_accessibility_id('1/4').click()
                driver.find_elements_by_class_name('XCUIElementTypeSwitch')[1].click()
                driver.find_elements_by_class_name('XCUIElementTypeTextField')[1].click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard plus').click()
                driver.find_element_by_accessibility_id('mock keyboard finish').click()
                driver.find_element_by_accessibility_id('请选择有效期').click()
                driver.swipe(200, 640, 200, 565, duration=sleep(3))
                driver.find_element_by_accessibility_id('完成').click()
                driver.find_element_by_accessibility_id('确认').click()
                driver.find_element_by_accessibility_id('确定').click()
            else:
                print u'价格不合适'
        except:
            pass
    driver.find_element_by_accessibility_id('back Icon').click()
    sleep(5)
    driver.find_element_by_accessibility_id('back Icon').click()
    sleep(5)
    try:
        driver.find_element_by_accessibility_id('市场').click()
    except:
        sleep(2)
        driver.find_element_by_accessibility_id('back Icon').click()
        driver.find_element_by_accessibility_id('市场').click()


