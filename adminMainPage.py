# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminMainPageManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class MainPageManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        if arg1=='':
            dynamicFiles = self.application.db.DynamicFiles
            banner = dynamicFiles.find_one({'_id': 'banner'})
            QandA = dynamicFiles.find_one({'_id': 'QandA'})
            termsOfService = dynamicFiles.find_one({'_id': 'termsOfService'})
            privacy = dynamicFiles.find_one({'_id': 'privacy'})
            about = dynamicFiles.find_one({'_id': 'about'})
            self.render('adminMainPage.html', banner=banner, QandA=QandA, termsOfService=termsOfService, privacy=privacy, about=about)
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        if arg1=='':
            banner = self.request.files['banner'][0]
            QandA = self.request.files['QandA'][0]
            termsOfService = self.request.files['termsOfService'][0]
            privacy = self.request.files['privacy'][0]
            about = self.request.files['about'][0]
            dynamicFiles = self.application.db.DynamicFiles.find({})
            
            self.redirect('/admin/mainPage')
            