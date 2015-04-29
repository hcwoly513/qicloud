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
import peewee
import pytz
from models import *

BASEPATH = os.path.dirname(__file__)
UPLOAD_FILE_PATH = os.path.join(BASEPATH, '/static/files')
TIMEZONE = 'Asia/Taipei'


class BaseHandler(tornado.web.RequestHandler):
    ''' This is a Base Setting. '''
    def get_current_user(self):
        return self.get_secure_cookie('account')


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
    password = str(password).encode('utf-8')
    return hashlib.sha1(password).hexdigest()

def checkSession():
    pass
