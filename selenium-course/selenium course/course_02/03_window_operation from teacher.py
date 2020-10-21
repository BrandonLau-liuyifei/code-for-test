__author__ = 'Administrator'
from selenium import webdriver
from time import sleep,localtime,strftime

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)

# 设置网页最小化
browser.minimize_window()
sleep(2)

# 设置网页最大化
browser.maximize_window()
sleep(2)

# 设置网页的大小
browser.set_window_size(300,100)
sleep(2)

# 设置网页最大化
browser.maximize_window()
sleep(2)

# 刷新网页
browser.refresh()
sleep(2)

# 网页前进后退需要先登录
# 使用sup的账号登录
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
sleep(2)
browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
sleep(2)
browser.find_element_by_xpath('//input[@id="button_submit"]').click()
sleep(2)

# 获取网页的URL和标签
URL = browser.current_url
print(URL)

title = browser.title
print(title)

# 获取当前登录用户的名字，需要先定位显示名字的元素信息，然后用text来获取
user_ele = browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/label')
username = user_ele.text
print(username)

# 截图，截登录后的首页
file_name = "D:\\zhaojia\\selenium\\selenium_105\\selenium_study\\picture\\首页截图.png"
browser.get_screenshot_as_file(file_name)

# 使用时间戳的方式截图
file_path = "D:\\zhaojia\\selenium\\selenium_105\\selenium_study\\picture\\"
file_name1 = "首页截图" + strftime("%Y%m%d%H%M%S",localtime()) + '.png'
browser.get_screenshot_as_file(file_path+file_name1)

# 网页的后退
browser.back()
sleep(2)

# 网页的前进
browser.forward()
sleep(2)

browser.quit()