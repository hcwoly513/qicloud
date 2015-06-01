# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminExamManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class ExamManage(common.BaseHandler):
    """
    Data Model
      _id               String    e.g. UUID4亂數
      examName          String    e.g. 國三數學考卷
      examInfo          String    e.g. XX數學考卷
      examType          String    e.g. 數學
      examFile          String    e.g. Gridfs file name
      uploadTime        Datetime  e.g. 2015-05-31T15:17:53.080Z
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Exam = db.Exam
        if arg1=='':
            exams = Exam.find()
            self.render('adminExam.html', exams=exams)
        elif arg1=='add':
            self.render('adminExamAdd.html')
        elif arg1=='modify':
            
            self.render('adminExamModify.html')
            
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        fs = common.grifsConnection()
        Exam = db.Exam
        if arg1=='':
            pass
        elif arg1=='add':
            pass
        elif arg1=='modify':
            pass