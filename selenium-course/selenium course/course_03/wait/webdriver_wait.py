__author__ = 'Administrator'
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8080/oa")

# 设置动态等待，判断所有符合class属性为logininput的元素全部加载完成，然后再执行后续脚本
# 用到的方法：presence_of_all_elements_located
WebDriverWait(browser,10).until(ec.presence_of_all_elements_located((By.CLASS_NAME,"loginInput")))
# 输入用户名
browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
# 输入密码
browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")

# 设置动态等待，判断登录按钮的value值是否出现预期的登录两个字
# 用到的方法：text_to_be_present_in_element_value
WebDriverWait(browser,10).until(ec.text_to_be_present_in_element_value((By.ID,"button_submit"),"登录"))
# 点击登录按钮
browser.find_element_by_xpath('//input[@id="button_submit"]').click()

# 点击新建事项之前，设置动态等待，判断新建事项是否可以点击
# 用到的方法：element_to_be_clickable
WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.LINK_TEXT,"新建事项")))
# 点击新建事项
browser.find_element_by_xpath('//a[text()="新建事项"]').click()

# 输入正文，需要切入框架，设置动态等待，判断框架是否加载出来
# 用到的方法：frame_to_be_available_and_switch_to_it
WebDriverWait(browser,10).until(ec.frame_to_be_available_and_switch_to_it("iframe_main"))
WebDriverWait(browser,10).until(ec.frame_to_be_available_and_switch_to_it("baidu_editor_0"))

# 设置动态等待，判断正文输入框是否出现
# 用到的方法：presence_of_element_located
WebDriverWait(browser,10).until(ec.presence_of_element_located((By.XPATH,"/html/body")))
# 定位正文输入框
zhengwen = browser.find_element_by_xpath('/html/body')
zhengwen.send_keys("今天天气有点凉")

# 点击清空文档，需要先对正文进行右击，然后切出框架，再设置动态等待，判断元素的文本值是否为期望的“清空文档”
# 用到的方法：text_to_be_present_in_element
ActionChains(browser).context_click(zhengwen).perform()
browser.switch_to.parent_frame()
WebDriverWait(browser,10).until(ec.text_to_be_present_in_element((By.XPATH,"/html/body/div[4]/div[5]/div/div[2]/div/div[2]/div/div[3]"),"清空文档"))
# 点击清空文档
browser.find_element_by_xpath('/html/body/div[4]/div[5]/div/div[2]/div/div[2]/div/div[3]').click()

# 对警告窗口进行操作，需要设置的动态等待，判断警告窗口是否出现
# 用到的方法：alert_is_present
alert = WebDriverWait(browser,10).until(ec.alert_is_present())

# 获取警告窗口中的文本，然后点击确定按钮
text = alert.text
print(text)
alert.accept()

browser.quit()