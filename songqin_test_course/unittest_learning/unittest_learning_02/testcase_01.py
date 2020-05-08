import unittest
from time import sleep

from ddt import ddt,data,unpack
from selenium import webdriver

#数据驱动
@ddt
class case1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
    def tearDown(self):
        self.driver.quit()
    # 测试数据
    @data("测码学院", "测码学院腾讯课堂", "软件测试")
   #测试用例代码
    def test_01(self,text):
        self.driver.find_element_by_id("kw").send_keys(text)
        self.driver.find_element_by_id("su").submit()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
        sleep(5)

if __name__=="__mian__":
    unittest.main()

    """
        组合数据输入的例子，如登录[登录,密码]
        @data([liuyifei,liuyifei1],[flying,flying1])
        @unpack    
    """

