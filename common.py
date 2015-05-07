# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: common.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import datetime
import smtplib
import hashlib
import os
from email.mime.text import MIMEText
import tornado.web
import pymongo
import peewee
import pytz
from torndsession import *
import models

BASEPATH = os.path.dirname(__file__)
UPLOAD_FILE_PATH = os.path.join(BASEPATH, '/static/files')
TIMEZONE = 'Asia/Taipei'

def init():
    pass


class BaseHandler(tornado.web.RequestHandler):
    ''' This is a Base Setting. '''
    def get_current_user(self):
        return self.get_secure_cookie('account')
    
    def checkLogin(self):
        member = self.current_user()
        if not member:
            self.write('請先登入！！')
            return None
        return member


def dbConnection():
    MONGODBUSERNAME = 'paulx'         # MongoDB 帳號
    MONGODBPASSWORD = 'asd56123zxc'   # MongoDB 密碼
    qicloud = pymongo.MongoClient('ds031842.mongolab.com', 31842).qicloud
    qicloud.authenticate(MONGODBUSERNAME, MONGODBPASSWORD)
    return qicloud

def sendEmail(receivers, subject, content):
    ''' This is a Gmail Sender. '''
    sender = 'hcwoly513@gmail.com'
    gmail_user = 'hcwoly513@gmail.com'
    gmail_pwd = 'siigzvhhojhjkbqk'
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = 'admin <admin@qicloud.biz>'
    msg['To'] = ';'.join(receivers)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(gmail_user, gmail_pwd)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    smtpObj.quit()

def now():
    datetimeNow = datetime.datetime.now()
    central = pytz.timezone(TIMEZONE)
    loc_d = central.localize(datetimeNow)
    return loc_d

def encryptPassword(password):
    password = password.encode('utf8')
    return hashlib.sha1(password).hexdigest()

def syncdb():
    qicloud = dbConnection()
    dynamicFiles = qicloud.DynamicFiles
    createDynamicFiles(dynamicFiles)

def createDynamicFiles(dynamicFiles):
    # English labels
    eLabels = ['banner', 'QandA', 'termsOfService', 'privacy', 'about', 'introVideo', 'navVideo']
    # Chinese labels
    cLabels = ['橫幅影像', '常見問答', '服務條款', '隱私權條款', '關於網站', '介紹影片', '導覽影片']
    for i in range(len(eLabels)):
        eLabel = eLabels[i]
        cLabel = cLabels[i]
        dynamicFiles.insert({'_id': eLabel, 'eLabel': eLabel, 'cLabel': cLabel, 'file': None, 'uploaded': False})

