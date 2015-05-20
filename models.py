# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Name:         models.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import peewee
import common

db = peewee.SqliteDatabase('qicloud.sqlite3')

def createDatabase():
    pass


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Announcements(BaseModel):        # 公告
    postTime = peewee.DateTimeField()  # 上傳日期
    announcement = peewee.CharField()  # 公告內容
    annStart = peewee.DateTimeField()  # 開始時間
    annEnd = peewee.DateTimeField()    # 結束時間


class DynamicFiles(BaseModel):                  # 動態文件
    eLabel = peewee.CharField(unique=True)      # English Label
    cLabel = peewee.CharField()                 # Chinese Label
    file = peewee.CharField(null=True)          # 檔案
    uploaded = peewee.BooleanField()            # 是否上傳


class Course(BaseModel):                      # 課程
    courseName = peewee.CharField()           # 課程名稱
    courseInfo = peewee.CharField()           # 課程簡介
    video = peewee.CharField()                # 課程影片
    uploadTime = peewee.DateTimeField()       # 上傳時間
    numClick = peewee.IntegerField(default=0) # 點擊率


class Member(BaseModel):                    # 會員
    account = peewee.CharField(unique=True) # 帳號
    password = peewee.CharField()           # 密碼
    image = peewee.CharField(null=True)     # 頭像
    email = peewee.CharField(unique=True)   # E-mail
    nickname = peewee.CharField()           # 暱稱
    signupDate = peewee.DateTimeField()     # 註冊日期
    last_login = peewee.DateTimeField()     # 最後一次登入時間


class CourseType(BaseModel):                   # 課程形態
    typeID = peewee.IntegerField(default=0)    # id
    typeName = peewee.CharField()              # 課程型態名稱
    image = peewee.CharField()                 # 圖片
    numUnits = peewee.IntegerField(default=0)  # 


class Unit(BaseModel):                   # 單元
    unitName = peewee.CharField()        # 單元名稱
    unitInfo = peewee.CharField()        # 單元簡介
    unitType = peewee.CharField()        # 單元形態
    numCourses = peewee.IntegerField()   # 課程數量
    teacherID = peewee.CharField()       # 講師ID
    image = peewee.BlobField()           # 單元圖片
    uploadTime = peewee.DateTimeField()  # 上傳時間


class Discussion(BaseModel):
    account = peewee.CharField()
    content = peewee.CharField()
    time = peewee.DateTimeField()
    
    
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
    image = peewee.CharField()
    teacherInfo = peewee.CharField()
    specialty = peewee.CharField()
    hotNum = peewee.IntegerField(default=0)


class Introduction(BaseModel):
    IntroductionTime = peewee.DateTimeField()
    logo = peewee.CharField()
    introduction = peewee.CharField()


class CourseSurvey(BaseModel):
    courseID = peewee.CharField()
    score = peewee.IntegerField()
    proposal = peewee.CharField()
    account = peewee.CharField()


class Highlight(BaseModel):
    title = peewee.CharField()
    content = peewee.CharField()
    uploadTime = peewee.DateTimeField()
    

