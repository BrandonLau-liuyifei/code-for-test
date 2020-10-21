__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

browser=webdriver.Firefox()
browser.get("http://localhost:8080/oa")
sleep(2)

browser.find_element_by_link_text("万年历").click()
sleep(1)
browser.find_element_by_link_text("计算器").click()
sleep(1)

windows=browser.window_handles
print(type(windows),len(windows))



browser.switch_to.window(windows[2])
browser.find_element_by_xpath("/html/body/div/form/table/tbody/tr[2]/td/table[3]/tbody/tr/td[5]/table/tbody/tr[3]/td[1]/input").click()
sleep(1)
browser.find_element_by_xpath("/html/body/div/form/table/tbody/tr[2]/td/table[3]/tbody/tr/td[5]/table/tbody/tr[4]/td[4]/input").click()
sleep(1)
browser.find_element_by_xpath("/html/body/div/form/table/tbody/tr[2]/td/table[3]/tbody/tr/td[5]/table/tbody/tr[3]/td[1]/input").click()
sleep(1)
browser.find_element_by_xpath("/html/body/div/form/table/tbody/tr[2]/td/table[3]/tbody/tr/td[5]/table/tbody/tr[4]/td[5]/input").click()
sleep(1)

browser.close()
sleep(2)

browser.switch_to.window(windows[1])
browser.find_element_by_id("nianjian").click()
sleep(3)
browser.find_element_by_id("yuejian").click()
sleep(3)

browser.close()
sleep(2)

browser.switch_to.window(windows[0])
browser.find_element_by_name("loginId").send_keys("sup")
browser.find_element_by_name("password").send_keys("s1234567")
browser.find_element_by_id("button_submit").click()
sleep(2)

browser.quit()



