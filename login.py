# -*- coding: utf-8
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.ioloop
import tornado.web
import motor
import common


class Login(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        self.render('login.html')
    
    @tornado.web.asynchronous
    def post(self):
        
        self.set_secure_cookie
        self.render('index.html', account=self.current_user)


class Logout(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        pass

class ForgetAccount(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        self.render('index.html')
        
    @tornado.web.asynchronous
    def post(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')