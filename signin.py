# -*- coding: utf-8
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
from models import *


class Signin(common.BaseHandler):
    def get(self):
        self.render('signin.html', errorMessage = '')
    
    def post(self):
        account = self.get_arguments('account')
        password = self.get_arguments('password')
        passwordSecond = self.get_arguments('passwordSecond')
        image = self.get_arguments('image')
        email = self.get_arguments('email')
        nickname = self.get_arguments('nickname')
        country = self.get_arguments('country')
        if email=='' or nickname=='' or account=='' or password=='' or passwordSecond=='':
            self.render(self, 'registration.html', errorMessage = '請填寫所有欄位')
            return
        if Member.get_by_id(account):
            self.render(self, 'registration.html', errorMessage = '帳號已經存在')
            return
        if password != passwordSecond:
            self.render(self, 'registration.html', errorMessage = '密碼與確認密碼不相符')
            return
        if Member.query(Member.email==email).fetch():
            self.render(self, 'registration.html', errorMessage = 'email已經存在')
            return