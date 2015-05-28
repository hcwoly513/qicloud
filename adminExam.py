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
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        Exam = self.application.db.Exam
        if arg1=='':
            self.render('adminExam.html')
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
        Exam = self.application.db.Exam
        if arg1=='':
            pass
        elif arg1=='add':
            examAdd(self)
        elif arg1=='modify':
            examModify(self)

def examAdd(handler):
    pass

def examModify(handler):
    pass