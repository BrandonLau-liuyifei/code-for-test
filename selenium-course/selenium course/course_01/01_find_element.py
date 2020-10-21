__author__ = 'Administrator'
from time import sleep
from selenium import webdriver

browser=webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
user_name_element=browser.find_element_by_class_name("loginInput")
user_name_element.send_keys("sup")
sleep(2)
user_password_element=browser.find_element_by_name("password").send_keys("s1234567")
sleep(2)
user_loggin_element=browser.find_element_by_id("button_submit").click()
sleep(2)
user_xinjianshixiang_element=browser.find_element_by_link_text("新建事项").click()
sleep(2)
user_yifdashixiang_element=browser.find_element_by_partial_link_text("已发").click()
sleep(2)
user_yibanshixiang_element=browser.find_element_by_css_selector("div.ui-accordion-content:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click()
sleep(2)
user_daifashixiang_element=browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/table/tbody/tr[11]/td/a/img").click()
sleep(2)
user_logout_element=browser.find_element_by_tag_name("a").click()
sleep(2)

# browser.quit()

user_wannianli_element=browser.find_element_by_link_text("万年历").click()
sleep(2)
