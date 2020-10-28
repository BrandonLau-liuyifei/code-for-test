from selenium import webdriver
import time,os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test_saveScreenshot(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        # 保存图片
        # self.driver.save_screenshot("baidu.png")
        # 添加时间戳
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        file_name = current_time+".png"
        # self.driver.save_screenshot(file_name)
        # 指定目录保存
        path = os.path.abspath('screenshot')
        file_path =  path + "/"+file_name
        self.driver.get_screenshot_as_file(file_path)




if __name__ == '__main__':
    case = TestCase()
    case.test_saveScreenshot()




"""
save_screenshot(filename)  保存截图到指定文件
get_screenshot_as_base64() 获取截图保存为64位编码
get_screenshot_as_file(filename) 获取截图保存使用完整的路径
get_screenshot_as_png() 获取当前截图的二进制文件数据
"""
