__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# 使用sup的账号登录
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
sleep(2)
browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
sleep(2)
browser.find_element_by_xpath('//input[@id="button_submit"]').click()
sleep(2)
# 点击新建事项
browser.find_element_by_xpath('//a[text()="新建事项"]').click()
sleep(2)
browser.switch_to.frame("iframe_main")
browser.switch_to.frame("baidu_editor_0")
# 首先导入actionchains模块，将驱动好的浏览器作为参数传入
# 调用context_click方法，需要将元素信息传入，最后调用perform来执行
zhengwen = browser.find_element_by_xpath('/html/body')
zhengwen.send_keys("今天心情还不错！")
ActionChains(browser).context_click(zhengwen).perform()
sleep(2)
# 点击清空文档，需要先切出框架到上一层框架，然后定位元素
browser.switch_to.parent_frame()
browser.find_element_by_xpath('//div[text()="清空文档"]').click()
sleep(2)
# 切入到警告窗口
alert = browser.switch_to.alert
# 获取警告窗口的提示信息
tips = alert.text
print(tips)
# 点击取消按钮
alert.dismiss()
sleep(2)

# 点击确定按钮

browser.quit()