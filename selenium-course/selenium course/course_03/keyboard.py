__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# 登录
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
sleep(2)
browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
sleep(2)
browser.find_element_by_xpath('//input[@id="button_submit"]').click()
sleep(2)

# 点击新建事项
browser.find_element_by_xpath('//a[contains(text(),"新建")]').click()
sleep(2)

# 输入正文需要切换框架
browser.switch_to.frame("iframe_main")
browser.switch_to.frame("baidu_editor_0")

# 定位正文输入框
zhengwen = browser.find_element_by_xpath('/html/body')
zhengwen.send_keys("今天是收假后第一天，有点不在状态，需要喝一个脉动。。。。。")
sleep(2)

# 在正文中换行5次
zhengwen.send_keys(Keys.ENTER*5)
sleep(2)

# 在正文中TAB键3次
zhengwen.send_keys(Keys.TAB*3)
sleep(2)

# 在正文中删除10次
zhengwen.send_keys(Keys.BACK_SPACE*10)
sleep(2)

# 在正文中全选、复制、粘贴10次
zhengwen.send_keys(Keys.CONTROL,'a')
sleep(2)
zhengwen.send_keys(Keys.CONTROL,'c')
sleep(2)
zhengwen.send_keys(Keys.CONTROL,'v'*10)
sleep(2)

browser.quit()