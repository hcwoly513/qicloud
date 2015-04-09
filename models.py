# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.ioloop
import tornado.web
import peewee

db = peewee.SqliteDatabase('qicloud.sqlite3')

class BaseModel(peewee.Model):
    class Meta:
        database = db


class Member(BaseModel): # 會員
    email = peewee.CharField(unique=True)
    nickname = peewee.CharField(unique=True)
    account = peewee.CharField(unique=True)
    password = peewee.CharField(unique=True)
    signupDate = peewee.DateField()



class CourseType(BaseModel): # 課程類型  E.g. 國文、英文、etc.
    typeID = peewee.IntegerField(default=0)
    typeNameT = peewee.CharField()
    typeNameS = peewee.CharField()
    image = peewee.CharField()
    numUnits = peewee.IntegerField(default=0)


class Unit(BaseModel): # 單元
    unitNameT = peewee.CharField()
    unitNameS = peewee.CharField()
    unitInfoT = peewee.CharField()
    unitInfoS = peewee.CharField()
    unitType = peewee.CharField()
    numCourses = peewee.IntegerField()
    teacherID = peewee.CharField()
    image = peewee.CharField()
    uploadTime = peewee.DateField()


class Course(BaseModel): # 課程
    unitID = peewee.CharField()
    courseNameT = peewee.CharField()
    courseNameS = peewee.CharField()
    courseInfoT = peewee.CharField()
    courseInfoS = peewee.CharField()
    video = peewee.CharField()
    freeCourse =  peewee.CharField()
    uploadTime = peewee.DateField()
    numClick = peewee.IntegerField(default=0)
    
    
class Favorite(BaseModel): # 最愛
    courseNameT = peewee.CharField()
    courseNameS = peewee.CharField()
    account = peewee.CharField()
    courseID = peewee.CharField()
    unitID = peewee.CharField()
    time = peewee.DateField()
    
   
    
    
class CourseDiscussion(BaseModel):  # 課程討論
    courseID = peewee.CharField()
    account = peewee.CharField()
    content = peewee.CharField()
    time = peewee.BooleanField()
    
    
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
    
    
class Response(BaseModel):  # 回應
    messageID = peewee.CharField()
    time = peewee.DateField()
    account = peewee.CharField()
    content = peewee.CharField()
    report = peewee.BooleanField(default=False)
    prosecutor = peewee.CharField()
    reportTime = peewee.DateField()

     
class Teacher(BaseModel):  # 教師簡介
    nameT = peewee.CharField()
    nameS = peewee.CharField()
    image = peewee.CharField()
    teacherInfoT = peewee.CharField()
    teacherInfoS = peewee.CharField()
    specialtyT = peewee.CharField()
    specialtyS = peewee.CharField()
    video = peewee.CharField()
    hotNum = peewee.IntegerField(default=0)
    
    
class DynamicFiles(BaseModel):  # 網站上的檔案  E.g. Banner、使用者條款 etc.
    eLabel = peewee.CharField()    # English label
    cLabel = peewee.CharField()    # Chinese label
    file = peewee.CharField()
    uploaded = peewee.BooleanField()


class Introduction(BaseModel):  # 介紹
    IntroductionTime = peewee.DateField()
    logo = peewee.CharField()
    introductionT = peewee.CharField()
    introductionS = peewee.CharField()
    

class Announcements(BaseModel):  # 公告
    postTime = peewee.DateField()
    announcementT = peewee.CharField()
    announcementS = peewee.CharField()
    annStart = peewee.DateField()
    annEnd = peewee.DateField()


class CourseSurvey(BaseModel):  # 課程調查
    courseID = peewee.CharField()
    score = peewee.IntegerField()
    proposal = peewee.CharField()
    account = peewee.CharField()


class Highlight(BaseModel):  # 熱門程度
    courseID = peewee.CharField()
    courseDate = peewee.DateField()
    account = peewee.CharField()