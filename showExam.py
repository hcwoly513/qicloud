# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         showExam.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Exam(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', '')
        Exam = self.application.db.Exam
        if arg1=='':
            #exams = Exam.find()
            self.render('examShow.html')