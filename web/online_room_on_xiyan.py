from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
dt=webdriver.Chrome()
url=''
dt.get(url)
dt.maximize_window()
sleep(1)
dt.find_element_by_id("loginform-username").send_keys("")
sleep(1)
dt.find_element_by_id("loginform-password").send_keys("")
sleep(1)
dt.find_element_by_name("login-button").submit()
sleep(1)
tabs=dt.find_elements_by_class_name('dropdown-toggle')
tabs[0].click()
dt.find_element_by_css_selector('#w2 > li:nth-child(4) > a').click()
dt.find_element_by_css_selector('#w1 > table > tbody > tr:nth-child(4) > td:nth-child(14) > a:nth-child(2) > span').click()
sel = dt.find_element_by_xpath('//*[@id="room-room_status"]')
Select(sel).select_by_value('mine')
dt.find_element_by_css_selector('#w0 > div:nth-child(22) > button').click()