import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_element(driver,*loc):
    e = driver.find_element(*loc)
    return e

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    loc1 = (By.ID,"kw")
    get_element(driver,*loc1).send_keys("极客时间")
    loc2 = (By.ID, "su")
    get_element(driver,*loc2).click()

    time.sleep(3)
    driver.quit()

"""

selenium webdriver对应的角色
    1.测试代码：自动化测试代码发送请求给浏览器驱动（地图）
    2.浏览器驱动：解析自动化测试代码、解析后发送给浏览器（司机）
    3.浏览器：执行浏览器去定发送的指令，完成测试步骤（出租车）

selenium webdriver和浏览器间的通信
    1.对于每一条测试脚本，一个http请求会被创建并且发送给浏览器的驱动
    2.浏览器驱动中包含了一个http server，用来接收这些http请求
    3.http server接受到的请求后根据请求来具体操作对应的浏览器
    4.浏览器执行具体的测试步骤
    5.浏览器将步骤执行结果返回给Http Server
    6.http server 又将结果返回给selenium脚本，如果错误的http代码我们会在控制太看到具体的报错信息。
"""
