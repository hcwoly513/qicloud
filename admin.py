# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: admin.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common


class Admin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        if arg1 == 'mainPageManage':
            self.render('adminMainPageManage.html')
        elif arg1 == 'memberManage':
            self.render('adminMemberManage.html')
        elif arg1 == 'courseManage':
            self.render('adminCourseManage.html')
        elif arg1 == 'teacherManage':
            self.render('adminTeacherManage.html')
        elif arg1 == 'examManage':
            self.render('adminExamManage.html')
        else:
            self.render('admin.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass


def mainPageManage(handler, method, arg1, arg2):
    if method == 'get': # Get Method.
        pass
    else: # Post Method.
        pass

def memberManage(handler, method, arg1, arg2):
    if method == 'get': # Get Method.
        pass
    else: # Post Method.
        pass

def courseManage(handler, method, arg1, arg2):
    if method =='get':
        pass
                
    else: #post
        pass                

def teacherManage(handler, method, arg1, arg2):
    if method == 'get': # Get Method.
        pass
    else: # Post Method.
        pass

def examManage(handler, method, arg1, arg2):
    if method == 'get': # Get Method.
        pass
    else: # Post Method.
        pass