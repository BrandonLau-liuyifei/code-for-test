__author__ = 'Administrator'
from selenium import webdriver
from time import sleep, strftime, localtime

browser=webdriver.Firefox()
browser.get("http://localhost:8080/oa")
sleep(2)

browser.minimize_window()
sleep(2)
browser.set_window_size(300,400)
sleep(2)
browser.maximize_window()
sleep(2)

browser.refresh()
sleep(2)

browser.find_element_by_name("loginId").send_keys("sup")
browser.find_element_by_name("password").send_keys("s1234567")
browser.find_element_by_id("button_submit").click()
sleep(2)

print("url地址是:%s title是:%s"%(browser.current_url,browser.title))
user=browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/label")
print(user.text)

file_name="C:\\Users\\Administrator\\Desktop\\lalala01.png"
browser.get_screenshot_as_file(file_name)

file_path="C:\\Users\\Administrator\\Desktop\\"
file_name1="jietu"+ strftime("%Y%m%d%H%M%S",localtime()) +".png"
browser.get_screenshot_as_file(file_path+file_name1)

browser.back()
sleep(2)
browser.forward()
sleep(2)

browser.quit()





