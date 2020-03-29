__author__ = 'Administrator'
from time import localtime,strftime
# 定义函数，时间生成当前时间的时间戳
def shijianchuo():
    # 获取当前时间
    current_time = localtime()
    # 将获取到的时间转换为标准的输出格式
    change_time = strftime("%Y%m%d%H%M%S",current_time)
    return change_time

# 定义函数，实现截图
def jietu(browser,text):
    # 确定截图的保存路径、图片的名字、图片的格式
    file_name = "D:\\zhaojia\\selenium\\selenium_105\\selenium_study\\picture\\"+text+shijianchuo()+".png"
    # 截图
    browser.get_screenshot_as_file(file_name)
