# -*- coding: utf-8
#!/usr/bin/env python
# Name:         signin.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:    © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Signin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        DynamicFiles = self.application.db.DynamicFiles
        banner = DynamicFiles.find_one({'_id': 'banner'})
        about = DynamicFiles.find_one({'_id': 'about'})
        privacy = DynamicFiles.find_one({'_id': 'privacy'})
        termsOfService = DynamicFiles.find_one({'_id': 'termsOfService'})
        QandA = DynamicFiles.find_one({'_id': 'QandA'})
        introVideo = DynamicFiles.find_one({'_id': 'introVideo'})
        arg1 = self.get_argument('arg1', None)
        self.render('signin.html', errorMessage = '', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
    
    @tornado.web.asynchronous
    def post(self):
        Member = self.application.db.Member
        account = self.get_argument('account', '')
        nickname = self.get_argument('nickname', '')
        password = self.get_argument('password', '')
        passwordSecond = self.get_argument('passwordSecond', '')
        email = self.get_argument('email', '')
        if account=='' or nickname=='' or password=='' or email=='':
            self.render('signin.html', errorMessage='請輸入所有欄位！')
            return
        if password != passwordSecond:
            self.render('signin.html', errorMessage='確認密碼不一致！')
            return
        if Member.find_one({'account': account}):
            self.render('signin.html', errorMessage='這個帳號已存在！')
            return
        if Member.find_one({'email': email}):
            self.render('signin.html', errorMessage='這個email已存在！')
            return
        password = common.encryptPassword(password)
        signupDate = common.now()
        last_login = common.now()
        Member.insert({'_id': account, 'account': account, 'password': password, 'image': None, 'email': email, 'nickname': nickname, 'signupDate': signupDate, 'last_login': last_login})
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')

