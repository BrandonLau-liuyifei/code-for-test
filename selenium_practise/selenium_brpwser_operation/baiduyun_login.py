#coding=utf8
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("https://pan.baidu.com/")
sleep(5)
driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
sleep(1)
driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("13922358271")
size=driver.find_element_by_id("TANGRAM__PSP_4__userName").size
print(size)
attribute=driver.find_element_by_id("TANGRAM__PSP_4__userName").get_attribute("type")
print(attribute)
result=driver.find_element_by_id("TANGRAM__PSP_4__userName").is_displayed()
print(result)


driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("flying")

"""text=driver.find_element_by_id("TANGRAM__PSP_4__password").text
print(text)"""

driver.find_element_by_id("TANGRAM__PSP_4__submit").submit()
sleep(1)

driver.quit()
