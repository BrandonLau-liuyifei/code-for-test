from selenium import webdriver


def baidu_serach():
    #创建一个chrome浏览器的session
    driver = webdriver.Chrome()
    #请求url
    driver.get('http://www.baidu.com')
    #静态等待
    driver.implicitly_wait(3)

#定位搜素框，输入搜索值
    driver.find_element_by_id("kw").send_keys("虚竹")
    driver.find_element_by_id("su").submit()
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

if __name__=="__main__":
    search = baidu_serach()