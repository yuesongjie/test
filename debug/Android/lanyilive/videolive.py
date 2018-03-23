# coding=utf-8
from time import sleep
sleep(2)
def videoliving(driver):
    videotab=driver.find_elements_by_id('com.lanyi.live:id/iv_tab_icon')
    videotab[1].click()
    sleep(5)
    try:
        tabs = driver.find_elements_by_id('com.lanyi.live:id/ll_tap')
    except:
        print u'视频直播查看失败'
        pass
    finally:
        chat = tabs[1]
        chat.click()
    sleep(2)
    # 返回主页
    driver.find_element_by_id('com.lanyi.live:id/btn_back').click()
    print u'视频直播查看成功'
