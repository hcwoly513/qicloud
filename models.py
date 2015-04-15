# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import peewee
from peewee import PeeweeException

db = peewee.SqliteDatabase('qicloud.sqlite3')

class BaseModel(peewee.Model):
    class Meta:
        database = db


class Member(BaseModel):                    # 會員
    id = peewee.IntegerField(primary_key = True)
    account = peewee.CharField(unique=True) # 帳號
    password = peewee.CharField()           # 密碼
    image = peewee.BlobField()              # 頭像
    email = peewee.CharField(unique=True)   # E-mail
    nickname = peewee.CharField()           # 暱稱
    signupDate = peewee.DateTimeField()     # 註冊日期
    country = peewee.CharField()            # 國別


class CourseType(BaseModel):                   # 課程形態
    typeID = peewee.IntegerField(default=0)    # id
    typeName = peewee.CharField()              # 課程型態名稱
    image = peewee.BlobField()                 # 圖片
    numUnits = peewee.IntegerField(default=0)  # 


class Unit(BaseModel):                   # 單元
    unitName = peewee.CharField()        # 單元名稱
    unitInfo = peewee.CharField()        # 單元簡介
    unitType = peewee.CharField()        # 單元形態
    numCourses = peewee.IntegerField()   # 課程數量
    teacherID = peewee.CharField()       # 講師ID
    image = peewee.BlobField()           # 單元圖片
    uploadTime = peewee.DateTimeField()  # 上傳時間


class Course(BaseModel):                      # 課程
    unitID = peewee.CharField()               # 單元ID
    courseName = peewee.CharField()           # 課程名稱
    courseInfo = peewee.CharField()           # 課程簡介
    video = peewee.BlobField()                # 課程影片
    uploadTime = peewee.DateTimeField()       # 上傳時間
    numClick = peewee.IntegerField(default=0) # 點擊率
    
    
class Favorite(BaseModel):
    courseName = peewee.CharField()
    account = peewee.CharField()
    courseID = peewee.CharField()
    unitID = peewee.CharField()
    time = peewee.DateTimeField()
    
    
class History(BaseModel):
    courseName = peewee.CharField()
    account = peewee.CharField()
    courseID = peewee.CharField()
    unitID = peewee.CharField()
    time = peewee.DateField()
    
    
class CourseDiscussion(BaseModel):
    courseID = peewee.CharField()
    account = peewee.CharField()
    content = peewee.CharField()
    time = peewee.DateTimeField()
    
    
class Topic(BaseModel):
    topicNameT = peewee.CharField()
    topicNameS = peewee.CharField()
    lastTime = peewee.DateField()
    lastAccount = peewee.CharField()
    messageTotal = peewee.IntegerField(default=0)
    
    
class Message(BaseModel):
    time = peewee.DateField()
    account = peewee.CharField()
    title = peewee.CharField()
    content = peewee.CharField()
    topicID = peewee.CharField()
    responseNum = peewee.IntegerField(default=0)
    report = peewee.BooleanField(default=False)
    prosecutor = peewee.CharField()
    reportTime = peewee.DateField()
    
    
class Response(BaseModel):
    messageID = peewee.CharField()
    time = peewee.DateField()
    account = peewee.CharField()
    content = peewee.CharField()
    report = peewee.BooleanField(default=False)
    prosecutor = peewee.CharField()
    reportTime = peewee.DateField()

     
class Teacher(BaseModel):
    name = peewee.CharField()
    image = peewee.BlobField()
    teacherInfo = peewee.CharField()
    specialty = peewee.CharField()
    hotNum = peewee.IntegerField(default=0)
    
    
class DynamicFiles(BaseModel):       # 動態文件
    id = peewee.CharField            # id
    eLabel = peewee.CharField()      # English Label
    cLabel = peewee.CharField()      # Chinese Label
    file = peewee.BlobField()        # 檔案
    uploaded = peewee.BooleanField() # 是否上傳


class Introduction(BaseModel):
    IntroductionTime = peewee.DateTimeField()
    logo = peewee.CharField()
    introductionT = peewee.CharField()
    introductionS = peewee.CharField()
    

class Announcements(BaseModel):
    postTime = peewee.DateTimeField()
    announcement = peewee.CharField()
    annStart = peewee.DateField()
    annEnd = peewee.DateField()


class CourseSurvey(BaseModel):
    courseID = peewee.CharField()
    score = peewee.IntegerField()
    proposal = peewee.CharField()
    account = peewee.CharField()


class HotStatistics(BaseModel):     # 
    courseID = peewee.CharField()
    courseDate = peewee.DateField()
    account = peewee.CharField()

