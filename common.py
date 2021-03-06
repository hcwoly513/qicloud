# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         common.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import datetime
import hashlib
import os
import random
import urllib
import uuid
import smtplib
from email.mime.text import MIMEText
import tornado.web
import pymongo
import gridfs
from bson.objectid import ObjectId
import pytz

BASEPATH = os.path.dirname(__file__)
TIMEZONE = 'Asia/Taipei'

def init():
    # Database initiated.
    db = dbConnection()
    if not 'DynamicFiles' in db.collection_names():
        dynamicFiles = db.DynamicFiles
        createDynamicFiles(dynamicFiles)
    if not 'Member' in db.collection_names():
        member = db.Member
        createAdmin(member)


class BaseHandler(tornado.web.RequestHandler):
    ''' This is a Base Setting. '''
    def get_current_user(self):
        account = self.get_secure_cookie('account')
        if account:
            account = account.decode('utf-8')
            return account
        else:
            return None


class ServeHandler(tornado.web.RequestHandler):
    def get(self, resource):
        if resource is None:
            return
        fs = gridfsConnection()
        resource = str(urllib.parse.quote(resource))
        file = fs.get(ObjectId(resource))
        self.set_header('Content-Type', file.content_type)
        self.set_header('Content-Length', file.length)
        self.write(file.read())


def dbConnection():
    # MongoDB Connection.
    MONGODBUSERNAME = ''  # MongoDB 帳號
    MONGODBPASSWORD = ''  # MongoDB 密碼
    db = pymongo.MongoClient('', 27017).qicloud
    db.authenticate(MONGODBUSERNAME, MONGODBPASSWORD)
    return db

def gridfsConnection():
    # Gridfs Connection
    db = dbConnection()
    fs = gridfs.GridFS(db)
    return fs

def sendEmail(receivers, subject, content):
    ''' This is a Gmail Sender. '''
    sender = 'your gmail account@gmail.com'
    gmail_user = 'your gmail account@gmail.com'
    gmail_pwd = 'your password'
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

def createAdmin(member):
    # Create Admin User.
    account = 'admin'
    password = encryptPassword('asd56123zxc')
    email = 'hcwoly513@gmail.com'
    nickname = '管理員'
    signupDate = now()
    member.insert_one({
        '_id': account,
        'account': account,
        'password': password,
        'email': email,
        'nickname': nickname,
        'signupDate': signupDate,
        })
    
def createDynamicFiles(dynamicFiles):
    # Create DynamicFiles.
    # English labels
    eLabels = ['banner', 'QandA', 'termsOfService', 'privacy', 'about', 'introVideo', 'navVideo']
    # Chinese labels
    cLabels = ['橫幅影像', '常見問答', '服務條款', '隱私權條款', '關於網站', '網站簡介', '導覽影片']
    for i in range(len(eLabels)):
        eLabel = eLabels[i]
        cLabel = cLabels[i]
        dynamicFiles.insert_one({
            '_id': eLabel,
            'eLabel': eLabel,
            'cLabel': cLabel,
            'file': None,
            'uploaded': False})


"""def createAnnouncement(announcement):
    # Create Announcement Example
    rnId = ''.join(str(uuid.uuid4()).split('-'))
    announcementName = ''
    announcementStart = ''
    announcementEnd = ''

def createCourse(course):
    # Create Example Course
    rnId = ''.join(str(uuid.uuid4()).split('-'))
    courseName = '國小數學'
    courseInfo = '就只是範例課程。'
    courseVideo = None
    courseTeacher = 'Teache1'
    courseType = '英文'
    uploadTime = now()
    #times = 0
    course.insert_one({
        '_id': rnId,
        'courseName': courseName,
        'courseInfo': courseInfo,
        'courseVideo': courseVideo,
        'courseTeacher': courseTeacher,
        'courseType': courseType,
        'uploadTime': uploadTime})

def createExam(exam):
    # Create Exam.
    rnId = ''.join(str(uuid.uuid4()).split('-'))
    examName = '範例數卷'
    examInfo = '範例使用'
    examType = '數學'
    examFile = None
    exam.insert_one({
        '_id': rnId,
        'examName': examName,
        'examInfo': examInfo,
        'examType': examType,
        'examFile': examFile})
    
def createGame(game):
    # Create Example Game.
    rnId = ''.join(str(uuid.uuid4()).split('-'))
    gameName = '2048'
    gameInfo = '2048 是一款規則簡單、容易上手的益智遊戲，規則雖簡單但是玩起來卻沒那麼簡單，需要稍微動一點腦經，思考一下步驟才能夠把數字組合起來！'
    gamePath = 'games/2048/index.html'
    uploadTime = now()
    times = 0
    game.insert_one({
        '_id': rnId,
        'gameName': gameName,
        'gameInfo': gameInfo,
        'gamePath': gamePath,
        'uploadTime': uploadTime,
        'times': times})

def createTeacher(teacher):
    # Create Teacher.
    rnId = ''.join(str(uuid.uuid4()).split('-'))
    teacherName = '王小明'
    teacherInfo = '畢業於台北帝國大學應用數學系'
    specialty = '國小數學、國中英文'
    teacher.insert_one({
        '_id': rnId,
        'teacherName': teacherName,
        'teacherInfo': teacherInfo,
        'specialty': specialty})"""
