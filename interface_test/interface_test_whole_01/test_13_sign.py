"""
鉴权方式：
session鉴权，安全系数不高
auth鉴权
sessiom鉴权
token鉴权
sign鉴权
oauth鉴权 第三方鉴权
"""
# 举例说明，微信支付签名
"""
业务背景
需要一个参数，sign
1.需要前面有参数，使用ASCII码排序
appid： wxd930ea5d5a258f4f
mch_id： 10000100
device_info： 1000
body： test
nonce_str： ibuaiVcKdpRxkhJA
2.排序后的参数名跟参数值使用&进行拼接
appid=wxd930ea5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA
3.拼接完成，还需要加入每个商户的key值也需要拼接
appid=wxd930ea5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA&key=key=192006250b4c09247ec02edce69f6a2d
4.拼接完成的字符串，进行加密处理，使用md5加密，加密后得到sign值
加密方式：网站上加密工具
或hash库

"""
import requests,hashlib
s='appid=wxd930ea5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA&key=key=192006250b4c09247ec02edce69f6a2d'
# 构建一个对象为md
md=hashlib.md5()
# 对字符串s进行编码
md.update(s.encode())
# res为生成后的加密值
res=md.hexdigest()
res=res.upper()
print(res)


