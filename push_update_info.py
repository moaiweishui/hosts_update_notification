# coding=utf-8

import sys
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

reload(sys)
sys.setdefaultencoding("utf-8")


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_email():
    from_addr = raw_input('From: ')
    password = raw_input('Password: ')
    to_addr = raw_input('To: ')
    smtp_server = 'smtp.163.com'

    msg = MIMEText('Hosts文件今天更新了！', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'LiuSS <%s>' % from_addr)
    msg['To'] = _format_addr(u'LiuSS <%s>' % to_addr)
    msg['Subject'] = Header(u'Hosts文件今天更新了没？', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()