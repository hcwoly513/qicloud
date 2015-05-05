# -*- coding: utf-8
#!/usr/bin/env python
# Name: login.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import string
import tornado.web
import common


class Login(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('login.html', errorMessage ='')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.get_arguments('account')
        password = self.get_arguments('password')
        pathName = self.get_argument('pathName', None)
        if not pathName:
            pathName = 'none'
        else:
            pathName = '/' + pathName
        if not account or not password:
            self.render('login.html', errorMessage = '請輸入帳號或密碼！！', pathName=pathName)
            return
        password = common.encryptPassword(password)
        result = Member.select().where(Member.account==account, Member.password==password).get()
        if not result:
            self.render('login.html', errorMessage='帳號或者密碼錯誤！！', pathName=pathName)
            return
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')


class Logout(common.BaseHandler):
    def get(self):
        self.clear_cookie('account')
        self.redirect('/')