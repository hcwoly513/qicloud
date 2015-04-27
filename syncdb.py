# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: syncdb.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import peewee
import common
from models import *

def create_tables():
    db.connect()
    db.create_tables([
        Announcements, DynamicFiles, Member, Course,
        Teacher, CourseType, Unit, CourseDiscussion,
        Topic, Message, Response, Introduction, CourseSurvey,
        Highlight])

def createDynamicFiles():
    # Note the order of these items are important, it determines the order the
    # items appear in 'base.html'
    # English labels
    eLabels = [ 'QandA', 'termsOfService', 'privacy', 'about']    
    # Chinese labels
    cLabels = [ '常見問答', '服務條款', '隱私權條款', '關於網站']
    
    for i in range(len(eLabels)):
        eLabel = eLabels[i]
        dynamicFiles = DynamicFiles()
        dynamicFiles.eLabel = eLabel
        dynamicFiles.cLabel = cLabels[i]
        dynamicFiles.file = None
        dynamicFiles.uploaded = False
        dynamicFiles.save()

if __name__ == '__main__':
    create_tables()
    createDynamicFiles()