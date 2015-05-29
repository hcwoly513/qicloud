# -*- coding: utf-8
#!/usr/bin/env python
# Name:         forget.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import random
import tornado.web
from bson.objectid import ObjectId
import common


class Forget(common.BaseHandler):
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
        if arg1=='getPassword':
            self.render('getPassword.html', errorMessage='', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
        else:
            return
    
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
        arg1 = self.get_argument('arg1', '')
        Member = db.Member
        if arg1=='getPassword':
            account = self.get_argument('account', '')
            email = self.get_argument('email', '')
            if not account or not email:
                self.render('getPassword.html', errorMessage='請輸入帳號或密碼！', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
            member = Member.find_one({'account': account, 'email': email})
            if member:
                self.render('getPassword.html', errorMessage='無此帳號歐！', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
            password = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(12))
            subject = '齊齊雲端密碼重置信件'
            content = "<html><p>以下為您重置後的密碼：</p>{0}</html>".format(password)
            common.sendEmail(member['email'], subject, content)
            enPassword = common.encryptPassword(password)
            Member.find_one_and_update({'account': member['account']}, {'$set': {'password': enPassword}})
            self.render('getPassword.html', errorMessage='您的密碼已重置。', banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)
