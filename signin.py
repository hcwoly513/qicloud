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
        if arg1=='checkAccount':
            account = self.get_argument('account', None)
            member = self.application.db.Member
            if member.find_one({'account': account}): # 
                self.write('TRUE')
            else:
                self.write('FALSE')
        elif arg1=='checkEmail':
            email = self.get_argument('email', None)
            if member.find_one({'email': email}):
                self.write('TRUE')
            else:
                self.write('FALSE')
        self.render('signin.html', errorMessage = '')
    
    @tornado.web.asynchronous
    def post(self):
        member = self.application.db.Member
        account = self.get_argument('account', None)
        nickname = self.get_argument('nickname', None)
        password = self.get_argument('password', None)
        passwordSecond = self.get_arguments('passwordSecond', None)
        email = self.get_argument('email', None)
        password = common.encryptPassword(password)
        signupDate = common.now()
        last_login = common.now()
        member.insert({'_id': account, 'account': account, 'password': password, 'image': None, 'email': email, 'nickname': nickname, 'signupDate': signupDate, 'last_login': last_login})
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')