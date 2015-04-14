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
        account = self.get_arguments('account')
        password = self.get_arguments('password')
        if not account or not password:
            self.render('login.html', error = '請輸入帳號或密碼！！')
            return
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')


class Logout(common.BaseHandler):
    def get(self):
        self.clear_cookie('account')
        self.redirect('/')