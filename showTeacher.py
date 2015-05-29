# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name:         views.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Teacher(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Teacher = db.Teacher
        if arg1=='':
            teachers = Teacher.find()
            self.render('teacherShow.html', teachers=teachers)
        elif arg1=='showOne':
            teacherId = self.get_argument('teacherId', '')
            teacher = Teacher.find_one({'_id': ObjectId(teacherId)})
            self.render('teacherShowOne.html', teacher=teacher)
