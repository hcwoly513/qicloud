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


class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')
    
    def post(self):
        account = self.get_argument('account')
        self.set_secure_cookie('account', account)
        self.render('index.html', account=self.current_user)


class Logout(tornado.web.RequestHandler):
    def get(self):
        if (self.get_argument('logout', None)):
            self.clear_cookie('username')
            self.render('index.html')