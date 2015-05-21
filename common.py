# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         common.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import datetime
import smtplib
import hashlib
import os
import random
from email.mime.text import MIMEText
import tornado.web
import pymongo
import gridfs
import pytz
import models

BASEPATH = os.path.dirname(__file__)
UPLOAD_FILE_PATH = os.path.join(BASEPATH, '/static/files')
TIMEZONE = 'Asia/Taipei'

def init():
    # Database initiated.
    db, fs = dbConnection()
    if not 'DynamicFiles' in db.collection_names():
        dynamicFiles = db.DynamicFiles
        createDynamicFiles(dynamicFiles)
    if not 'Member' in db.collection_names():
        member = db.Member
        createAdmin(member)
    '''
    if not 'Course' in db.collection_names():
        course = db.Course
        createCourse(course)
    if not 'Game' in db.collection_names():
        game = db.game
        createGame(game)
    if not 'Teacher' in db.collection_names():
        teacher = db.Teacher
        createTeacher(teacher)
    if not 'Exam' in db.collection_names():
        exam = db.Example
        createExam(exam)
    if not 'Highlight' in db.collection_names():
        highlight = db.Highlight
        createHighlight(highlight)'''
    


class BaseHandler(tornado.web.RequestHandler):
    ''' This is a Base Setting. '''
    def get_current_user(self):
        account = self.get_secure_cookie('account')
        if account:
            account = account.decode('utf-8')
        return account


class ServeHandler(tornado.web.RequestHandler):
    def get(self, resource):
        fs = self.application.fs
        file = fs.get_last_version(resource)
        self.set_header('Content-Type', file.content_type)
        self.set_header('Content-Length', file.length)
        self.write(file.read())


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file = self.request.files['file1'][0]
        rnFile = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(64))
        file_id = fs.put(file['body'], content_type=file['content_type'], filename=rnFile)
        self.write(rnFile)


def dbConnection():
    # Database connection.
    MONGODBUSERNAME = 'qicloud'         # MongoDB 帳號
    MONGODBPASSWORD = 'asd56123zxc'   # MongoDB 密碼
    db = pymongo.MongoClient('qicloud.biz', 27017).qicloud
    db.authenticate(MONGODBUSERNAME, MONGODBPASSWORD)
    fs = gridfs.GridFS(db)
    return db, fs

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
    password = password.encode(encoding='utf-8')
    return hashlib.sha1(password).hexdigest()

"""def syncdb():
    qicloud = dbConnection()
    dynamicFiles = qicloud.DynamicFiles
    member = qicloud.Member
    createDynamicFiles(dynamicFiles)
    createAdmin(member)"""

def createDynamicFiles(dynamicFiles):
    # create DynamicFiles.
    # English labels
    eLabels = ['banner', 'QandA', 'termsOfService', 'privacy', 'about']
    # Chinese labels
    cLabels = ['橫幅影像', '常見問答', '服務條款', '隱私權條款', '關於網站']
    for i in range(len(eLabels)):
        eLabel = eLabels[i]
        cLabel = cLabels[i]
        dynamicFiles.insert({
            '_id': eLabel,
            'eLabel': eLabel,
            'cLabel': cLabel,
            'file': None,
            'uploaded': False})

def createAdmin(member):
    # Create Admin User.
    account = 'admin'
    password = encryptPassword('asd56123zxc')
    image = None
    email = 'hcwoly513@gmail.com'
    nickname = '管理員'
    signupDate = now()
    last_login = now()
    member.insert({
        '_id': account,
        'account': account,
        'password': password,
        'image': image,
        'email': email,
        'nickname': nickname,
        'signupDate': signupDate,
        'last_login': last_login})

