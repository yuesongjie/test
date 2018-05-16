# coding=utf-8
from time import sleep
def personalcenter(driver):
    centertab=driver.find_elements_by_id('com.lanyi.live:id/iv_tab_icon')
    centertab[4].click()
    sleep(1)
    driver.find_element_by_id('com.lanyi.live:id/layout_message').click()
    sleep(1)
    driver.find_elements_by_id('com.lanyi.live:id/tv_tab_title')[1].click()
    sleep(1)
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.find_element_by_id('com.lanyi.live:id/layout_feedback').click()
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.find_element_by_id('com.lanyi.live:id/layout_help').click()
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="转到上一层级"]').click()
    driver.find_element_by_id('com.lanyi.live:id/text_attendance').click()
    driver.quit()