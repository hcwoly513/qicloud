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
        self.render('signin.html', errorMessage = '')
    
    def post(self):
        member = Member()
        account = self.get_arguments('account')
        password = self.get_arguments('password')
        passwordSecond = self.get_arguments('passwordSecond')
        image = self.request.files.get('image', None)
        email = self.get_arguments('email')
        nickname = self.get_arguments('nickname')
        country = self.get_arguments('country')
        if email=='' or nickname=='' or account=='' or password=='' or passwordSecond=='':
            self.render(self, 'signin.html', errorMessage = '請填寫所有欄位')
            return
        if Member.select():
            self.render(self, 'signin.html', errorMessage = '帳號已經存在')
            return
        if password != passwordSecond:
            self.render(self, 'signin.html', errorMessage = '密碼與確認密碼不相符')
            return
        if Member.query(Member.email==email).fetch():
            self.render(self, 'signin.html', errorMessage = 'email已經存在')
            return
        member.account = account
        member.password = password
        member.image = image
        member.email = email
        member.nickname = nickname
        member.signupDate = common.now()
        member.save()
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')