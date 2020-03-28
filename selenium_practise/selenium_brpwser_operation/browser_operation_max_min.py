from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print("最大化浏览器")
driver.maximize_window()
sleep(2)
print("浏览器设置窗口大小")
driver.set_window_size(300,400)
sleep(3)
driver.quit()


