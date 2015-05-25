# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminMainPageManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import random
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
            introVideo = dynamicFiles.find_one({'_id': 'introVideo'})
            navVideo = dynamicFiles.find_one({'_id': 'navVideo'})
            self.render('adminMainPage.html', banner=banner, QandA=QandA, termsOfService=termsOfService, privacy=privacy, about=about, introVideo=introVideo, navVideo=navVideo)
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        dynamicFiles = self.application.db.DynamicFiles
        fs = self.application.fs
        if arg1=='':
            banner = self.get_argument('banner', '')
            QandA = self.get_argument('QandA', '')
            termOfService = self.get_argument('termOfService', '')
            privacy = self.get_argument('privacy', '')
            about = self.get_argument('about', '')
            introVideo = self.get_argument('introVideo', '')
            navVideo = self.get_argument('navVideo', '')
            if banner!= '':
                banner = self.request.files['banner'][0]
                rnName = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(64))
                file_id = fs.put(banner['body'], content_type=banner['content_type'], filename=rnName)
                banners = dynamicFiles.update_one({'_id', 'banner'}, {'$set': {'file': rnName}})
            if QandA!= '':
                QandA = self.request.files['QandA'][0]
            if termOfService!= '':
                termsOfService = self.request.files['termsOfService'][0]
            if privacy!= '':
                privacy = self.request.files['privacy'][0]
            if about!= '':
                about = self.request.files['about'][0]
            if introVideo!= '':
                introVideo = self.request.files['introVideo'][0]
            if navVideo!= '':
                navVideo = self.request.files['navVideo'][0]
            self.render('admin.html', pathName='/admin')
            