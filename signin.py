# -*- coding: utf-8
#!/usr/bin/env python
# Name: signin.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

from __future__ import absolute_import, division, print_function, with_statement

import tornado.web
import common
from models import *


class Signin(common.BaseHandler):
    def get(self):
        self.render('signin.html', errorMessage = '123')
    
    def post(self):
        member = Member()
        account = self.get_arguments('account')
        nickname = self.get_arguments('nickname')
        password = self.get_arguments('password')
        passwordSecond = self.get_arguments('passwordSecond')
        email = self.get_arguments('email')
        if email=='' or nickname=='' or account=='' or password=='' or passwordSecond=='':
            self.render('signin.html', errorMessage = '請填寫所有欄位')
            return
        if Member.select():
            self.render('signin.html', errorMessage = '帳號已經存在')
            return
        if password != passwordSecond:
            self.render('signin.html', errorMessage = '密碼與確認密碼不相符')
            return
        if Member.select().where(Member.email==email):
            self.render('signin.html', errorMessage = 'email已經存在')
            return
        member.account = account
        member.password = password
        member.email = email
        member.nickname = nickname
        member.signupDate = common.now()
        member.last_login = common.now()
        member.save()
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')