from selenium import webdriver
from PIL import Image
import time
import pytesseract
# 使用pytessract和pillow解决不复杂的验证码
def test_01():
    # 打开页面
    browser  = webdriver.Chrome()
    browser.get("http://www.jpress.io/user/register")
    browser.maximize_window()

    #获取验证码
    t = time.time()
    picture_name_01 = str(t) + ".png"
    browser.save_screenshot(picture_name_01)

    ce = browser.find_element_by_id("captchaimg")
    print(ce.location,ce.size)
    left = ce.location["x"]
    top = ce.location["y"]
    right = left + ce.size["width"]
    down = top + ce.size["height"]
    im = Image.open(picture_name_01)

    # 抠图-验证码图片
    image = im.crop((left,top,right,down))
    t = time.time()
    picture_name_02 = str(t) + ".png"
    image.save(picture_name_02)
    browser.quit()

def test_02():
    image_02 = Image.open('1604835221.5250099.png')
    str = pytesseract.image_to_string(image_02)
    print(str)
'''
使用pytessract和pillow解决不复杂的验证码
01 截屏整个页面
02 selenium获取元素的左顶点，和宽高，计算出左上点、左下点、右上点、右下点
03 根据坐标抠图
04 使用pytessract模块进行验证
'''
'''
macOS
brew install tesseract
This formula contains only the "eng", "osd", and "snum" language data files.
If you need any other supported languages, run `brew install tesseract-lang`.
'''

# 使用第三方ai平台进行识别

def test_03(ShowapiRequest=None):
    from test_17_project.lib.ShowapiRequest import ShowapiRequest
    r = ShowapiRequest("http://route.showapi.com/184-4","424254","5899434fd7774bf49c46457b32145560")
    r.addFilePara("image","1604835221.5250099.png")
    # r.addBodyPara("img_base64", "")
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise","0")
    res = r.post()
    print(res.json()["showapi_res_body"]["Result"])  # 返回信息

"""
1.https://www.showapi.com/apiGateway/view?apiCode=184 注册账号
2.选择识别类型，例如识别英文数字验证码
3.下载sdk,放入lib中
4.根据帮助文档进行验证
"""