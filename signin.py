# -*- coding: utf-8
#!/usr/bin/env python
# Name: signin.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common


class Signin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_arguments('arg1')
        if arg1 == 'checkAccount':
            account = self.get_arguments('account')
            if Member.select().where(Member.account==account).get():
                self.write('TRUE')
            else:
                self.write('FALSE')
        elif arg1 == 'checkEmail':
            email = sel.get_arguments('email')
            if Member.select().where(Member.email==email).get():
                self.write('TRUE')
            else:
                self.write('FALSE')
        elif arg1 == 'checkAccountEmail':
            account = self.get_arguments('account')
            email = sel.get_arguments('email')
            if Member.select().where(Member.account==account, Member.email==email).get():
                self.write('TRUE')
            else:
                self.write('FALSE')
        else:
            self.render('signin.html', errorMessage = '')
    
    @tornado.web.asynchronous
    def post(self):
        member = Member()
        account = self.get_arguments('account')
        nickname = self.get_arguments('nickname')
        password = self.get_arguments('password')
        passwordSecond = self.get_arguments('passwordSecond')
        email = self.get_arguments('email')
        if email=='' or nickname=='' or account=='' or password=='' or passwordSecond=='':
            self.render('signin.html', pathName = pathName, errorMessage = '請填寫所有欄位')
            return
        if Member.select().where(Member.account==account).get():
            self.render('signin.html', pathName = pathName, errorMessage = '帳號已經存在')
            return
        if password != passwordSecond:
            self.render('signin.html', pathName = pathName, errorMessage = '密碼與確認密碼不相符')
            return
        if Member.select().where(Member.email==email).get():
            self.render('signin.html', pathName = pathName, errorMessage = 'email已經存在')
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