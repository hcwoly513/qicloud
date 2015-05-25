# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminCourseManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class CourseManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        if arg1=='':
            self.render('adminCourse.html')
        elif arg1=='add':
            self.render('adminCourseAdd.html')
        elif arg1=='modify':
            self.render('adminCourseModify.html')

    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        if arg1=='':
            pass
        elif arg1=='add':
            courseAdd(self)
        elif arg1=='modify':
            courseModify(handler)

def courseAdd(handler):
    pass

def courseModify(handler):
    pass