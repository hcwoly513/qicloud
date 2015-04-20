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
        member = self.current_user()
        if member is None or member.account != 'admin':
            return
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        if arg1=='courseManage':
            courseManage(self, 'get', arg1, arg2)
        elif arg1=='teacherManage':
            teacherManage(self, 'get', member, arg2)
        elif arg1=='messageManage':
            messageManage(self, 'get', member, arg2)
        elif arg1=='courseTypeManage':
            courseTypeManage(self, 'get', arg1, arg2)
        elif arg1=='mainPageManage':
            mainPageManage(self, 'get', arg1, arg2)
        elif arg1=='announcementManage':
            announcementManage(self, 'get', arg1, arg2)
        elif arg1=='memberManage':
            memberManage(self, 'get', arg1, arg2)
    
    def post(self):
        member = self.current_user()
        if member is None or member.account != 'admin':
            return
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        if arg1=='courseManage':
            courseManage(self, 'post', arg1, arg2)
        elif arg1=='teacherManage':
            teacherManage(self, 'post', member, arg2)
        elif arg1=='messageManage':
            messageManage(self, 'post', member, arg2)
        elif arg1=='courseTypeManage':
            courseTypeManage(self, 'post', arg1, arg2)
        elif arg1=='mainPageManage':
            mainPageManage(self, 'post', arg1, arg2)
        elif arg1=='announcementManage':
            announcementManage(self, 'post', arg1, arg2)
        elif arg1=='memberManage':
            memberManage(self, 'post', arg1, arg2)


def courseManage(handler, method, arg1, arg2):
    if method =='get':
        pass
                
    else: #post
        pass                

def teacherManage(handler, method, member, arg2):
    if method=='get':
        pass
        
    else:   #method =='post'
        pass

def messageManage(handler, method, member, arg2):
    localTime = common.now() 
    if method=='get':
        pass          
    else:   #method =='post'
        pass

def courseTypeManage(handler, method, arg1, arg2):
    if method=='get':
        pass
    else : #method=post
        pass

def mainPageManage(handler, method, arg1, arg2):
    if method=='get':
        pass
    else: #POST
        pass

def memberManage(handler, method, arg1, arg2):
    if method == 'get':
        pass
    else:
        pass    

def announcementManage(handler, method, arg1, arg2):
    if method=='get':
        pass
    else:   #method =='post'
        pass
