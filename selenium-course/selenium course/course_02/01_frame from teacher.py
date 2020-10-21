__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

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
# 输入标题，需要先切入框架
browser.switch_to.frame("iframe_main")
browser.find_element_by_xpath('//input[@id="subject"]').send_keys("今天是selenium第二天，快要放假了！")
sleep(2)
# 点击流程，已经在框架中，不需要切框架
browser.find_element_by_xpath('//input[@id="trackInput"]').click()
sleep(2)
# 点击集团职能部，需要先从之前的框架中切出，然后还需要切入另外一个框架
browser.switch_to.default_content()

liucheng1 = browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/components/selectemp/selectempforcollaborate.jsp?uuid=")]')
browser.switch_to.frame(liucheng1)
browser.find_element_by_xpath('//span[text()="集团职能部"]').click()
sleep(2)
# 点击总经办
browser.find_element_by_xpath('//span[text()="总经办"]').click()
sleep(2)
# 点击添加全部按钮
browser.find_element_by_xpath('//button[@class="button" and @title="添加全部"]').click()
sleep(2)
# 点击确定按钮
browser.find_element_by_xpath('//button[contains(text(),"确定")]').click()
sleep(2)

# 点击流程2中的确定按钮，需要从原来的框架中切出，然后再切入第二个框架
browser.switch_to.default_content()
liucheng2 = browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/components/flowchart/newflowchart_svg.jsp?uuid=")]')
browser.switch_to.frame(liucheng2)
browser.find_element_by_xpath('//button[contains(text(),"确定")]').click()
sleep(2)
# 输入正文，需要先切出原来的框架，然后再切入正文所在的框架
browser.switch_to.default_content()
browser.switch_to.frame("iframe_main")
browser.switch_to.frame("baidu_editor_0")
browser.find_element_by_xpath('/html/body').send_keys("今天主要讲框架的切换、网页的操作、鼠标的操作、警告窗口的操作！")
sleep(2)

# 点击立即发送按钮，需要切出到上一层框架
browser.switch_to.parent_frame()
browser.find_element_by_xpath('//button[@id="button_send"]').click()
sleep(2)

# 点击确定按钮，需要切换到默认框架
browser.switch_to.default_content()
browser.find_element_by_xpath('//input[@value="确定" and @class="d-button"]').click()
sleep(2)



browser.quit()
