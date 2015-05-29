# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         showCourse.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Course(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Course = db.Course
        if arg1=='':
            courses = Course.find()
            self.render('courseShow.html', courses=courses)
        elif arg1=='showOne':
            courseId = self.get_argument('courseId', '')
            course = Course.find_one({'_id': courseId})
            self.render('courseShowOne.html', course=course)
