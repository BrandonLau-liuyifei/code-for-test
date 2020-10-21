__author__ = 'Administrator'
from selenium_day3.shijianchuo.def_shijianchuo import jietu
from time import sleep
# 定义函数，通过xpath来判断元素是否存在，如果存在则返回true，否则返回False
def element_exit_by_xpath(browser,elexpath):
    if browser.find_element_by_xpath(elexpath):
        return True
    else:
        return False

# 定义函数，结合try和except来判断元素是否存在，通过link_text来判断
def element_exit_by_link_text(browser,text):
    try:
        browser.find_element_by_link_text(text)
        return True
    except:
        return False

# 定义函数，实现判断链接是否存在，如果存在则截图，否则输出“链接未找到”
def text_click_jietu(browser,text):
    result = element_exit_by_link_text(browser,text)
    if result==True:
        browser.find_element_by_link_text(text).click()
        sleep(2)
        jietu(browser,text)
    else:
        print("链接未找到。。。。。")