# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import datetime, smtplib
from email.mime.text import MIMEText
import tornado.web
from models import *

def init():
    pass


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('account')
    
    def checkSession(self):
        return
    
def sendEmail(receivers, msg):
    sender = 'admin@qicloud.biz'
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, msg)
    

def now():
    return datetime.datetime.now()+ datetime.timedelta(hours=8)