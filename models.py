# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import peewee

db = peewee.SqliteDatabase('qicloud.sqlite3')

class BaseModel(peewee.Model):
    class Meta:
        database = db


class Member(BaseModel):
    account = peewee.CharField()
    image = peewee.BlobField()
    email = peewee.CharField()
    nickname = peewee.CharField()    
    password = peewee.CharField()    
    signupDate = peewee.DateTimeField()


class CourseType(BaseModel):
    typeID = peewee.IntegerField(default=0)
    typeName = peewee.CharField()
    image = peewee.CharField()
    numUnits = peewee.IntegerField(default=0)


class Unit(BaseModel):
    unitName = peewee.CharField()
    unitInfo = peewee.CharField()
    unitType = peewee.CharField()
    numCourses = peewee.IntegerField()
    teacherID = peewee.CharField()
    image = peewee.BlobField()
    uploadTime = peewee.DateTimeField()


class Course(BaseModel):
    unitID = peewee.CharField()
    courseName = peewee.CharField()
    courseInfo = peewee.CharField()
    video = peewee.BlobField()
    uploadTime = peewee.DateTimeField()
    numClick = peewee.IntegerField(default=0)
    
    
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
    time = ndb.DateProperty()
    
    
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
    
    
class DynamicFiles(BaseModel):
    eLabel = peewee.CharField()    # English label
    cLabel = peewee.CharField()    # Chinese label
    file = peewee.CharField()
    uploaded = peewee.BooleanField()


class Introduction(BaseModel):
    IntroductionTime = peewee.DateField()
    logo = peewee.CharField()
    introductionT = peewee.CharField()
    introductionS = peewee.CharField()
    

class Announcements(BaseModel):
    postTime = peewee.DateField()
    announcementT = peewee.CharField()
    announcementS = peewee.CharField()
    annStart = peewee.DateField()
    annEnd = peewee.DateField()


class CourseSurvey(BaseModel):
    courseID = peewee.CharField()
    score = peewee.IntegerField()
    proposal = peewee.CharField()
    account = peewee.CharField()


class HotStatistics(BaseModel):
    courseID = peewee.CharField()
    courseDate = peewee.DateField()
    account = peewee.CharField()

