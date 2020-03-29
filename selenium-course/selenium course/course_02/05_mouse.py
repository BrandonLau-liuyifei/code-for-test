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

# 在个人设置后面的三角形上悬停
# 首先导入actionchains模块，将驱动好的浏览器作为参数传入
# 调用move_to_element方法，需要将元素信息传入，最后调用perform来执行
personal_setting = browser.find_element_by_xpath('//span[@class="m-btn-downarrow"]')
ActionChains(browser).move_to_element(personal_setting).perform()
sleep(2)
# 点击常用语设置
browser.find_element_by_xpath('//div[text()="常用语设置"]').click()
sleep(2)
# 关闭常用语设置
browser.find_element_by_xpath('//a[@class="d-close"]').click()
sleep(2)
# 点击新建事项
browser.find_element_by_xpath('//a[text()="新建事项"]').click()
sleep(2)
# 点击流程，需要切换框架
browser.switch_to.frame("iframe_main")
browser.find_element_by_xpath('//input[@id="trackInput"]').click()
sleep(2)
# 点击集团职能部，需要切回默认框架，再切入框架
browser.switch_to.default_content()
liucheng1 = browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/components/selectemp/selectempforcollaborate.jsp?uuid=")]')
browser.switch_to.frame(liucheng1)
browser.find_element_by_xpath('//span[text()="集团职能部"]').click()
sleep(2)
browser.find_element_by_xpath('//span[text()="总经办"]').click()
sleep(2)
# 双击邢佳军
# 首先导入actionchains模块，将驱动好的浏览器作为参数传入
# 调用double_click方法，需要将元素信息传入，最后调用perform来执行
leader = browser.find_element_by_xpath('/html/body/div[2]/select/option[1]')
ActionChains(browser).double_click(leader).perform()
sleep(2)
# 点击确定按钮
browser.find_element_by_xpath('//button[contains(text(),"确定")]').click()
sleep(2)
# 切换到流程2的框架中，点击确定按钮
browser.switch_to.default_content()
liucheng2 = browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/components/flowchart/newflowchart_svg.jsp?uuid=")]')
browser.switch_to.frame(liucheng2)
# 点击确定按钮
browser.find_element_by_xpath('//button[contains(text(),"确定")]').click()
sleep(2)

# 右击正文输入框，需要切换框架
browser.switch_to.default_content()
browser.switch_to.frame("iframe_main")
browser.switch_to.frame("baidu_editor_0")
# 首先导入actionchains模块，将驱动好的浏览器作为参数传入
# 调用context_click方法，需要将元素信息传入，最后调用perform来执行
zhengwen = browser.find_element_by_xpath('/html/body')
ActionChains(browser).context_click(zhengwen).perform()
sleep(2)

browser.quit()