# -*- coding: utf-8
#!/usr/bin/env python
# Name:         login.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import string
import pymongo
import gridfs
import tornado.web
import common


class Login(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('login.html', errorMessage ='')
    
    @tornado.web.asynchronous
    def post(self):
        member = self.application.db.Member
        account = self.get_argument('account', None)
        password = self.get_argument('password', None)
        pathName = self.get_argument('pathName', None)
        password = common.encryptPassword(password)
        memberGet = member.find_one({'account': account})
        if memberGet['account'] != account or memberGet['password'] != password:
            self.render('login.html', errorMessage = '帳號或者密碼錯誤！')
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')


class Logout(common.BaseHandler):
    def get(self):
        self.clear_all_cookies()
        self.redirect('/')