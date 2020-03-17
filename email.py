'''
邮件发送需要准备哪些内容
1.邮件的发送方（发送方地址，发送方客户端授权密码，SMTP服务器地址smtp.2980.com）
2.邮件内容
3.邮件接收方'''

import smtplib
from email.mime.text import MIMEText

sender = ""