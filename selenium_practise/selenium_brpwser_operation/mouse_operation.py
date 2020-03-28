#coding=utf8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://pan.baidu.com/")
sleep(5)
driver.maximize_window()#最大化窗口
driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
sleep(1)
driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("13922358271")#输入账户名
size=driver.find_element_by_id("TANGRAM__PSP_4__userName").size
print(size)
attribute=driver.find_element_by_id("TANGRAM__PSP_4__userName").get_attribute("type")#返回元素属性
print(attribute)
result=driver.find_element_by_id("TANGRAM__PSP_4__userName").is_displayed()#判断元素可视
print(result)
driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("flying")#输入密码
driver.find_element_by_id("TANGRAM__PSP_4__submit").submit()
sleep(1)
button=driver.find_element_by_class_name("vcode-slide-button")
target=driver.find_elements_by_xpath('//*[@id="vcode-spin-button547"]')
ActionChains(driver).drag_and_drop(button,target).perform()
# driver.quit()