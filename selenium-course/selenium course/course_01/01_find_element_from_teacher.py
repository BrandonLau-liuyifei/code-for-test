__author__ = 'Administrator'
from time import sleep
from selenium import webdriver

# 打开浏览器
browser = webdriver.Firefox()
sleep(2)
# 输入URL
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# 输入用户名，需要先模拟眼睛的动作，找到用户名输入框，然后手才能输入
username_ele = browser.find_element_by_class_name('loginInput')
username_ele.send_keys("sup")
sleep(2)
# 输入密码，需要先模拟眼睛的动作，找到密码输入框，然后手才能输入
browser.find_element_by_name("password").send_keys("s1234567")
sleep(2)
# 点击登录按钮，需要先模拟眼睛的动作，找到登录按钮，然后手才能点击
browser.find_element_by_id("button_submit").click()
sleep(2)
# 点击新建事项，通过链接内容来定位
browser.find_element_by_link_text("新建事项").click()
sleep(2)
# 点击已发事项，通过部分链接内容来定位
browser.find_element_by_partial_link_text("已发").click()
sleep(2)

# 点击已办事项上方的图片，可以通过css的方式来定位
browser.find_element_by_css_selector("div.ui-accordion-content:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click()
sleep(2)

# 点击待发事项上方的图片，可以通过xpath的方式来定位
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/table/tbody/tr[11]/td/a/img").click()
sleep(2)

# 点击退出登录，通过标签名称来定位
browser.find_element_by_tag_name("a").click()
sleep(2)

# 关闭浏览器
browser.quit()

