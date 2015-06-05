# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminMainPageManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class MainPageManage(common.BaseHandler):
    """
    Data Model
      _id                   String   e.g. 
      eLabel                String   e.g. 
      cLabel                String   e.g. 
      file                  String   e.g. 
      uploaded              Boolean  e.g. 
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        fs = common.gridfsConnection()
        DynamicFiles = db.DynamicFiles
        banner = DynamicFiles.find_one({'_id': 'banner'})
        QandA = DynamicFiles.find_one({'_id': 'QandA'})
        termsOfService = DynamicFiles.find_one({'_id': 'termsOfService'})
        privacy = DynamicFiles.find_one({'_id': 'privacy'})
        about = DynamicFiles.find_one({'_id': 'about'})
        introVideo = DynamicFiles.find_one({'_id': 'introVideo'})
        navVideo = DynamicFiles.find_one({'_id': 'navVideo'})
        if arg1=='':
            self.render('adminMainPage.html', banner=banner, QandA=QandA, termsOfService=termsOfService, privacy=privacy, about=about, introVideo=introVideo, navVideo=navVideo)
        elif arg1=='banner':
            self.render('adminMainPageBanner.html')
        elif arg1=='QandA':
            self.render('adminMainPageQandA.html')
        elif arg1=='termsOfService':
            self.render('adminMainPageTermsOfService.html')
        elif arg1=='privacy':
            self.render('adminMainPagePrivacy.html')
        elif arg1=='about':
            self.render('adminMainPageAbout.html')
        elif arg1=='introVideo':
            self.render('adminMainPageIntroVideo.html')
        elif arg1=='navVideo':
            self.render('adminMainPageNavVideo.html')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        fs = common.gridfsConnection()
        DynamicFiles = db.DynamicFiles
        if arg1=='banner':
            file = self.request.files['banner'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'banner'}, {'$set': {'file': file_id, 'uploaded': True}})
        elif arg1=='QandA':
            file = self.request.files['QandA'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'QandA'}, {'$set': {'file': file_id, 'uploaded': True}})
        elif arg1=='termsOfService':
            file = self.request.files['termsOfService'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'termsOfService'}, {'$set': {'file': file_id, 'uploaded': True}})
        elif arg1=='privacy':
            file = self.request.files['privacy'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'privacy'}, {'$set': {'file': file_id, 'uploaded': True}})
        elif arg1=='about':
            file = self.request.files['about'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'about'}, {'$set': {'file': file_id, 'uploaded': True}})
        elif arg1=='introVideo':
            file = self.request.files['introVideo'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'introVideo'}, {'$set': {'file': file_id, 'uploaded': True}})
        elif arg1=='navVideo':
            file = self.request.files['navVideo'][0]
            file_id = fs.put(file['body'], content_type=file['content_type'], filename=file['filename'])
            DynamicFiles.find_one_and_update({'_id': 'navVideo'}, {'$set': {'file': file_id, 'uploaded': True}})
            