# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: admin.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
import adminCourseManage
import adminExamManage
import adminMainPageManage
import adminMemberManage
import adminTeacherManage


class Admin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        if arg1 == 'courseManage':
            adminCourseManage.courseManage(self, 'get', arg1, arg2)
        elif arg1 == 'examManage':
            adminExamManage.examManage(self, 'get', arg1, arg2)
        elif arg1 == 'mainPageManage':
            adminMainPageManage.mainPageManage(self, 'get', arg1, arg2)
        elif arg1 == 'memberManage':
            adminMemberManage.memberManage(self, 'get', arg1, arg2)
        elif arg1 == 'teacherManage':
            adminTeacherManage.teacherManage(self, 'get', arg1, arg2)
        else:
            self.render('admin.html')
    
    @tornado.web.asynchronous
    def post(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        if arg1 == 'courseManage':
            adminCourseManage.courseManage(self, 'post', arg1, arg2)
        elif arg1 == 'examManage':
            adminExamManage.examManage(self, 'post', arg1, arg2)
        elif arg1 == 'mainPageManage':
            adminMainPageManage.mainPageManage(self, 'post', arg1, arg2)
        elif arg1 == 'memberManage':
            adminMemberManage.memberManage(self, 'post', arg1, arg2)
        elif arg1 == 'teacherManage':
            adminTeacherManage.teacherManage(self, 'post', arg1, arg2)
        else:
            self.redirect('/admin')

