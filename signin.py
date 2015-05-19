# -*- coding: utf-8
#!/usr/bin/env python
# Name:         signin.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:    © PaulX 2015

import tornado.web
import common


class Signin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_argument('arg1', None)
        arg2 = self.get_argument('arg2', None)
        
        self.render('signin.html', errorMessage = '')
    
    @tornado.web.asynchronous
    def post(self):
        member = self.application.db.Member
        account = self.get_arguments('account')[0]
        nickname = self.get_arguments('nickname')[0]
        password = self.get_arguments('password')[0]
        passwordSecond = self.get_arguments('passwordSecond')[0]
        email = self.get_arguments('email')[0]
        password = common.encryptPassword(password)
        member.insert({'_id': account, 'account': account, 'nickname': nickname, 'password': password, 'email': email})
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')