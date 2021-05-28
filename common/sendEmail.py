# coding=utf-8 
"""
@Time    : 2020/05/24  下午 12:36
@Author  : hnm
@FileName: sendEmail.py
@IDE     : PyCharm
"""

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = '784165503@qq.com'
password = "sbowmxjybgljbcff"
sender = username
receivers = ','.join(['huangnamei6800@dingtalk.com'])
# 读取时间戳
now = time.strftime('%Y-%m-%d-%H-%M-%S')

def email(report):
	# 设置请求头信息
	msg = MIMEMultipart()
	msg['Subject'] = now + '碳银接口测试报告'  # 邮件名
	msg['From'] = sender
	msg['To'] = receivers

	jpgpart = MIMEApplication(open(report, 'rb').read())
	jpgpart.add_header('Content-Disposition', 'attachment', filename='碳银接口测试报告.html')
	msg.attach(jpgpart)

	#发送邮件
	client = smtplib.SMTP()
	client.connect('smtp.qq.com')
	client.login(username, password)
	client.sendmail(sender, receivers, msg.as_string())
	client.quit()
	print("邮件发送成功，请查看")


if __name__ == "__main__":
	re = r"C:\tanwinjob\interface test\apiautotest-tanwin\report\2021-05-17 17_31_27测试报告.html"
	#for i in range(10):
		#time.sleep(2)
		#email(re)
	email(re)