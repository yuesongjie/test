# coding=utf-8
from time import sleep
sleep(3)
def news(driver,x,y):
    driver.find_element_by_id('com.lanyife.futures:id/navigation_news').click()
    driver.find_element_by_id('com.lanyife.futures:id/school_tv').click()
    driver.find_elements_by_id('com.lanyife.futures:id/video_layout')[1].click()
    sleep(3)
    driver.find_element_by_accessibility_id('button-play').click()
    sleep(3)
    driver.find_element_by_id('com.lanyife.futures:id/back_iv').click()
    # driver.find_element_by_id('com.lanyife.futures:id/back_iv').click()
    xmyllist = driver.find_elements_by_id('com.lanyife.futures:id/album_title_tv')
    for listentitle in xmyllist:
        print listentitle.get_attribute('name')

    driver.find_element_by_id('com.lanyife.futures:id/news_tv').click()
    alltabs = driver.find_elements_by_id('com.lanyife.futures:id/tv_tab_title')
    for tab in alltabs:
        tab.click()
    driver.swipe(int(x) / 2, int(y) / 2, int(x) / 2, int(y) / 200, duration=sleep(5))
    a = driver.find_elements_by_id('com.lanyife.futures:id/title')[2].click()
    sleep(2)
    title = driver.find_elements_by_class_name('android.view.View')[9].get_attribute('name')
    print title
    driver.find_element_by_id('com.lanyife.futures:id/back_layout').click()
