#coding=utf-8
from selenium import webdriver
from time import sleep
#确定登录地址
def loginurl(url):
   if url=='x':
       return 'http://www.ycl999.com/back/'
   elif url=='b':
       return 'http://www.xiyan98.com/back/'
   else:
       return 'http://www.xidu98.com/back/'

print 'a.七福帮 b.七指禅'
urls=raw_input('请输入网站字母代号以进入系统：')
url=urls.lower()
dis=loginurl(url)
print dis
#登录系统
browser=webdriver.Chrome()
browser.get(dis)
browser.maximize_window()
#输入用户名、密码
sleep(1)
browser.find_element_by_id("loginform-username").send_keys("")
sleep(1)
browser.find_element_by_id("loginform-password").send_keys("")
sleep(1)
browser.find_element_by_name("login-button").submit()
sleep(1)
#选择进入直播室
livingrooms= browser.find_elements_by_css_selector(".superClassNav .l-enterbroadcast")
livingrooms[0].click()
#激活直播区域
browser.find_element_by_class_name("LiveListView").click()
sleep(2)
#发送操盘单
liveEditor = browser.find_element_by_css_selector('.LiveContainer .EditorContainer')
liveEditor.find_element_by_css_selector('.ZTabs__tabItem:nth-child(2)').click()  # 切换到"高手操盘"界面
def getOptions():#下拉选项
    selector = ".ant-select-dropdown:not(.ant-select-dropdown-hidden) .ant-select-dropdown-menu-item"
    return browser.find_elements_by_css_selector(selector)
sleep(1)
selects = browser.find_elements_by_css_selector(".OperateRecordForm__formLeft .ant-form-item")
selects[0].find_element_by_css_selector('.ant-select-selection__placeholder').click()
sleep(2)
options = getOptions()#产品选择
options[1].click()
sleep(2)
if url=='b':
    browser.find_element_by_id("deliveryDate").send_keys('19991231')
    # selects[2].find_element_by_css_selector('.ant-select-selection__placeholder').click()  # 选择"操作方向"
    # options = getOptions()
    # options[mine].click()  # 选择做空
    optionn=selects[2].find_elements_by_css_selector('.ant-radio-button-wrapper')
    optionn[1].click()
    sleep(2)
    browser.find_element_by_id("strategyPoint").send_keys("1000")
    browser.find_element_by_id("strategyTargetProfit").send_keys("800")
    browser.find_element_by_id("strategyTargetLose").send_keys("1200")

    sleep(2)
else:
    browser.find_element_by_id("deliveryDate").send_keys('19991231')
    selects[2].find_element_by_css_selector('.ant-select-selection__placeholder').click()  # 选择"操作方向"
    options = getOptions()
    options[1].click()  # 选择做空
    sleep(2)
    browser.find_element_by_id("strategyPoint").send_keys("1000")
    browser.find_element_by_id("strategyTargetProfit").send_keys("800")
    browser.find_element_by_id("strategyTargetLose").send_keys("1200")
    sleep(2)
browser.find_element_by_id("strategyReason").send_keys("gg")
sleep(2)
browser.find_element_by_css_selector(".ant-col-11 .ant-form-item-control .ant-btn").click()#点击发送
browser.quit()