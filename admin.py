# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: admin.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
from models import *


class Admin(common.BaseHandler):
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        if arg1 == 'mainPageManage':
            self.render('adminMainPageManage.html')
        elif arg1 == 'memberManage':
            self.render('adminMemberManage.html')
        elif arg1 == 'teacherManage':
            self.render('adminTeacherManage.html')
        else:
            self.render('admin.html')
    
    def post(self):
        pass


def courseManage(handler, method, arg1, arg2):
    if method =='get':
        pass
                
    else: #post
        pass                


def example(handler, method, arg1, arg2):
    if method == 'get': # Get Method.
        pass
    else: # Post Method.
        pass