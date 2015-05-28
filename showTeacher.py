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
        arg1 = self.get_argument('arg1', None)
        Teacher = self.application.db.Teacher
        if arg1=='':
            self.render('teacherShow.html')
        elif arg1=='showOne':
            self.render('teacherShowOne.html')
        
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', None)
        Teacher = self.application.db.Teacher