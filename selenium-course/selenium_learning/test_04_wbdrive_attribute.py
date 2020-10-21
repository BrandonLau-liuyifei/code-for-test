from selenium import webdriver
import time

class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        # self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)   #获取浏览器名称
        print(self.driver.current_url)  #获取当前页面的网址
        print(self.driver.title)   #获取当前页面的title
        print(self.driver.current_window_handle)  #获取当前窗口的具柄
        print(self.driver.window_handles)  #获取所有窗口的句柄
        print(self.driver.page_source)    #获取页面的源码
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.driver.back()    # 页面返回
        self.driver.find_element_by_id("kw").send_keys("极客时间")
        time.sleep(3)
        self.driver.refresh()   #页面刷新
        time.sleep(3)
        self.driver.forward()    #页面前进
        time.sleep(3)
        self.driver.close()   #页面关闭

    def test_window(self):
        self.driver.find_element_by_partial_link_text("新闻").click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                time.sleep(2)

if __name__ == "__main__":
    case = testCase()
    # case.test_prop()
    # case.test_method()
    case.test_window()


"""
webdriver的属性：
    driver.name 浏览器名称
    driver.current_url 当前url
    driver.title 当前页面标题
    driver.page_source 当前页面源码
    driver.current_windows_handle 窗口句柄
    driver.window_handles 当前窗口所有句柄
webdriver的方法：  
    driver.back() 浏览器后退
    driver.forward() 浏览器前进
    driver.refresh() 浏览器刷新
    driver.close() 浏览器关闭
    driver.quit() 浏览器退出
    driver.switch_to.frame() 切换到frame
    driver.switch_to.alert() 切换到alert
    driver.switch_to.active_element() 切换到活动元素
"""