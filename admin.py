# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         admin.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:    © PaulX 2015

import tornado.web
import common
import adminCourseManage
import adminExamManage
import adminGameManage
import adminMainPageManage
import adminMemberManage
import adminTeacherManage


class Admin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_argument('arg1', None)
        arg2 = self.get_argument('arg2', None)
        self.render('admin.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass
    

