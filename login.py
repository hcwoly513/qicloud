# -*- coding: utf-8
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common


class Login(common.BaseHandler):
    def get(self):
        self.render('login.html')
    
    def post(self):
        account = self.get_argument('account')
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')


class Logout(common.BaseHandler):
    def get(self):
        self.clear_cookie('account')
        self.redirect('/')

class ForgetAccount(common.BaseHandler):
    def get(self):
        pass
    
    def post(self):
        pass

