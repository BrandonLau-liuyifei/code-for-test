__author__ = 'Administrator'
from selenium import webdriver
from time import sleep

browser=webdriver.Firefox()
sleep(2)
browser.get("http://127.0.0.1:8080/oa")
sleep(2)
# login
browser.find_element_by_class_name("loginInput").send_keys("sup")
sleep(2)
browser.find_element_by_name("password").send_keys("s1234567")
sleep(2)
browser.find_element_by_id("button_submit").click()
browser.find_element_by_xpath('//a[text()="新建事项"]').click()
sleep(2)
# 输入标题，需要先切入框架
browser.switch_to.frame("iframe main")
browser.find_element_by_id("subject").send_keys("这是一个试验")
sleep(2)
# 创建流程，已在框架内，不需要再次进入
browser.find_elements_by_id("trackInput").click()
sleep(2)
# 选择"集团职能部"，需要熊之前的框架切出，再从另一个框架切入
browser.switch_to.default_content()
# 切入流程1的框架，需要先定位这个框架，得到对象以后再切入
process1=browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/components/selectemp/selectempforcollaborate.jsp?uuid=")]')
browser.switch_to.frame(process1)
browser.find_elements_by_id("DeptTreeDiv_48_span").click()
sleep(2)
browser.find_element_by_class_name("button").click()
sleep(2)
browser.find_elements_by_id("instanceType_1")
sleep(2)
browser.find_element_by_tag_name("button")
sleep(2)
# 切入流程2的框架，需要先定位这个框架，得到对象以后再切入
browser.switch_to.default_content()
process2=browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/components/flowchart/newflowchart_svg.jsp?uuid=")]')
browser.switch_to.frame(process2)
sleep(2)
browser.find_element_by_tag_name("button")
# 切入正文框架框架，需要先定位这个框架，得到对象以后再切入
browser.switch_to.default_content()
browser.switch_to.frame("iframe main")
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








