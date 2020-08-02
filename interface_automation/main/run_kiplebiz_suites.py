#coding:utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
# from email import encoders

def send_mail(report):
    now_time = time.strftime("%Y-%m-%d %H：%M：%S")
    report_name = os.path.basename(report)
    subject = 'kiplebiz接口自动化测试报告'+now_time
    sender = 'dan.li@greenpacket.com.cn'
    receiver = ['dan.li@greenpacket.com.cn',]

    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['from'] = sender
    msg['To'] = ";".join(receiver)
    #读取文件
    with open(report, 'rb') as f:
        send_att = f.read()
    att = MIMEText(send_att, 'html', 'utf-8')
    # new_att = encoders.encode_base64(att)
    # 创建邮件内容
    text = "kiplepay接口测试，测试结果请查看附件!!!"
    # text_plain = MIMEText(new_att, 'plain', 'utf-8')
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)
    # 发送附件
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = %s' % (report_name)
    msg.attach(att)
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("dan.li@greenpacket.com.cn", "Lidan123!!!")
    try:
        smtp.sendmail(sender, receiver, msg.as_string())
        print('email was sent successfully!')
    except smtplib.SMTPException:
        print('fail to send this email!')
    finally:
        smtp.quit()


if __name__ == '__main__':
    get_path = os.path.dirname(os.getcwd())
    # 定义测试用例的目录
    test_dir = get_path+'/test_suites/kiplebiz'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='debug_test_kiplepay*.py')

    # 取当前日期时间
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    html_report = get_path +'/report/kiplebiz/' + 'kiplepay'+now_time + '_result.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="kiplepay接口测试"
                            )
    runner.run(suit)
    fp.close()
    # 发送报告
    send_mail(html_report)

