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
from bson.objectid import ObjectId
import tornado.web
import common


class Login(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        db = common.dbConnection()
        DynamicFiles = db.DynamicFiles
        banner = DynamicFiles.find_one({'_id': 'banner'})
        about = DynamicFiles.find_one({'_id': 'about'})
        privacy = DynamicFiles.find_one({'_id': 'privacy'})
        termsOfService = DynamicFiles.find_one({'_id': 'termsOfService'})
        QandA = DynamicFiles.find_one({'_id': 'QandA'})
        introVideo = DynamicFiles.find_one({'_id': 'introVideo'})
        arg1 = self.get_argument('arg1', '')
        if arg1=='':
            self.render('login.html', errorMessage ='', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
        elif arg1=='checkAccount':
            pass
        elif arg1=='checkEmail':
            pass
    
    @tornado.web.asynchronous
    def post(self):
        db = common.dbConnection()
        DynamicFiles = db.DynamicFiles
        banner = DynamicFiles.find_one({'_id': 'banner'})
        about = DynamicFiles.find_one({'_id': 'about'})
        privacy = DynamicFiles.find_one({'_id': 'privacy'})
        termsOfService = DynamicFiles.find_one({'_id': 'termsOfService'})
        QandA = DynamicFiles.find_one({'_id': 'QandA'})
        introVideo = DynamicFiles.find_one({'_id': 'introVideo'})
        Member = db.Member
        account = self.get_argument('account', '')
        password = self.get_argument('password', '')
        if not account or not password:
            self.render('login.html', errorMessage='請輸入帳號密碼！', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
            return
        password = common.encryptPassword(password)
        memberGet = Member.find_one({'account': account})
        if not memberGet:
            self.render('login.html', errorMessage = '無此使用者！', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
            return
        if memberGet['account'] != account or memberGet['password'] != password:
            self.render('login.html', errorMessage = '帳號或者密碼錯誤！', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
            return
        self.set_secure_cookie('account', account, httponly=True)
        self.redirect('/')


class Logout(common.BaseHandler):
    def get(self):
        self.clear_all_cookies()
        self.redirect('/')