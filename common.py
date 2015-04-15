# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import datetime, smtplib, hashlib
from email.mime.text import MIMEText
import tornado.web
import peewee
from models import *

def init():
    if not DynamicFiles.select():
        createDynamicFiles()


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('account')
    
    
def sendEmail(receivers, subject, content):
    sender = 'hcwoly513@gmail.com'
    gmail_user = 'hcwoly513@gmail.com'
    gmail_pwd = 'siigzvhhojhjkbqk'
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = 'admin <admin@qicloud.biz'
    msg['To'] = ';'.join(receivers)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(gmail_user, gmail_pwd)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    smtpObj.quit()    

def now():
    return datetime.datetime.now()+ datetime.timedelta(hours=8)

def encryptPassword(password):
    password = password.encode('utf-8')
    return hashlib.sha1(password).hexdigest()

def createDynamicFiles():
    # Note the order of these items are important, it determines the order the
    # items appear in 'base.html'
    # English labels
    eLabels = [ 'banner', 'QandA', 'termsOfService', 'privacy', 'about', 'introVideo', 'navVideo']    
    # Chinese labels
    cLabels = [ '橫幅影像', '常見問答', '服務條款', '隱私權條款', '關於網站', '介紹影片', '導覽影片']
    
    for i in range(len(eLabels)):
        eLabel = eLabels[i]
        dynamicFiles = DynamicFiles()
        dynamicFiles.eLabel = eLabel
        dynamicFiles.cLabel = cLabels[i]
        dynamicFiles.file = None
        dynamicFiles.uploaded = False
        dynamicFiles.save()


