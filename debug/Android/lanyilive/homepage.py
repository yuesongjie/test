#coding=utf-8
from time import sleep
def home(driver):
    sleep(2)
    try:
        driver.find_element_by_id('com.lanyi.live:id/btn_close').click()
    except:
        print u'未发现首页弹窗'
    try:
        driver.find_element_by_id('com.lanyi.live:id/img_close').click()
    except:
        print u'未发现签到弹窗'
    sleep(3)
    cataarea = driver.find_element_by_id('com.lanyi.live:id/list_category')
    categorylists = cataarea.find_elements_by_class_name('android.widget.LinearLayout')
    try:
        teacherboard=categorylists[0]
        #stocksignboard = categorylists[0]
        videoreplay = categorylists[1]
        stockschool = categorylists[2]
        stockreference = categorylists[3]
    except:
        sleep(5)
        teacherboard = categorylists[0]
        # stocksignboard = categorylists[0]
        videoreplay = categorylists[1]
        stockschool = categorylists[2]
        stockreference = categorylists[3]
    def back():
        driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
        sleep(2)
    stockschool.click()
    sleep(2)
    schoolarea = driver.find_elements_by_xpath(
        '//android.webkit.WebView[@content-desc="股市学院"]/android.widget.ListView/android.view.View')
    # 第一部分
    sleep(5)
    schoolarea[0].click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//android.view.View[@content-desc="文章列表"]')
    except:
        print u'页面打开失败'
        pass
    else:
        pass
    finally:
        back()
    # 第二部分
    schoolarea[1].click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//android.view.View[@content-desc="文章列表"]')
    except:
        print u'页面打开失败'
        pass
    else:
        pass
    finally:
        back()
    # 第三部分
    schoolarea[2].click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//android.view.View[@content-desc="文章列表"]')
    except:
        print u'页面打开失败'
        pass
    else:
        pass
    finally:
        back()
        print u'查看股市学院成功'
    back()
    teacherboard.click()
    allarea=driver.find_element_by_id('android:id/content')
    innerarea=allarea.find_element_by_class_name('android.widget.LinearLayout')
    inarea=innerarea.find_element_by_class_name('android.widget.ListView')
    oneteacher=inarea.find_elements_by_class_name('android.widget.LinearLayout')[1]
    oneteacher.click()
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    back()
    back()
    # stocksignboard.click()
    # switchout = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    # switchout[1].click()
    # driver.find_element_by_id('com.lanyi.live:id/radio_time').click()
    # sleep(3)
    # stocklist1 = driver.find_element_by_id('com.lanyi.live:id/view_list')
    # stocklist1.click()
    # sleep(5)
    # cprice = driver.find_element_by_id('com.lanyi.live:id/text_price_current').get_attribute('name')
    # if cprice == '--':
    #     print u'获取行情失败'
    # else:
    #     sleep(2)
    #     print u'查看股票看板成功'
    # back()
    # back()
    sleep(2)
    videoreplay.click()
    try:
        driver.find_element_by_id('com.lanyi.live:id/btn_start')
    except:
        print u'未获取到视频信息'
        pass
    else:
        driver.find_element_by_id('com.lanyi.live:id/list_record').click()
        sleep(2)
    finally:
        driver.find_element_by_id('com.lanyi.live:id/btn_back').click()
        print u'查看视频回放成功'
    stockreference.click()
    openaccount = driver.find_element_by_id('com.lanyi.live:id/text_actionbar').get_attribute('name')
    if openaccount == u'股票开户，立领绝密内参':
        print u'成功打开绝密内参'
    else:
        print u'打开绝密内参失败'
    back()

    livetabarea1 = driver.find_element_by_id('com.lanyi.live:id/layout_tabs')
    livetabarea2 = livetabarea1.find_element_by_class_name('android.widget.HorizontalScrollView')
    livetabarea3 = livetabarea2.find_element_by_class_name('android.widget.LinearLayout')
    livetabarea4 = livetabarea3.find_elements_by_class_name('android.widget.RelativeLayout')
    mskp = livetabarea4[0]
    lltt = livetabarea4[1]
    sckx = livetabarea4[2]
    try:
        mskp.click()
    except:
        print u'获取图文信息失败'
        pass
    else:
        driver.find_element_by_id('com.lanyi.live:id/text_content').click()
        sleep(3)
        back()
    try:
        lltt.click()
    except:
        print u'获取图文信息失败'
        pass
    else:
        driver.find_element_by_id('com.lanyi.live:id/view_list').click()
        sleep(3)
        back()
    try:
        sckx.click()
    except:
        print u'获取图文信息失败'
        pass
    else:
        driver.find_element_by_id('com.lanyi.live:id/text_title').click()
        sleep(3)
        back()
    print u'查看图文直播成功'
