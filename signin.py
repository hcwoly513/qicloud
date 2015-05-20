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
            account = self.get_arguments('account')[0]
            member = self.application.db.Member
            if member.find_one({'account': account}) is None:
                self.write('FALSE')
            else:
                self.write('TRUE')
        elif arg1=='checkEmail':
            email = self.get_arguments('email')[0]
            if member.find_one({'email': email}) is None:
                self.write('FALSE')
            else:
                self.write('TRUE')
        self.render('signin.html', errorMessage = '')
    
    @tornado.web.asynchronous
    def post(self):
        member = self.application.db.Member
        account = self.get_arguments('account')[0]
        nickname = self.get_arguments('nickname')[0]
        password = self.get_arguments('password')[0]
        passwordSecond = self.get_arguments('passwordSecond')[0]
        email = self.get_arguments('email')[0]
        if password != passwordSecond:
            self.render('signin.html', errorMessage='你的密碼確認不一致！')
        password = common.encryptPassword(password)
        signupDate = common.now()
        last_login = common.now()
        member.insert({'_id': account, 'account': account, 'password': password, 'image': None, 'email': email, 'nickname': nickname, 'signupDate': signupDate, 'last_login': last_login})
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')