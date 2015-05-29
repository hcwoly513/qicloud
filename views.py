# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: views.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class MainHandler(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        db = common.dbConnection()
        DynamicFiles = db.DynamicFiles
        common.init()
        banner = DynamicFiles.find_one({'_id': 'banner'})
        about = DynamicFiles.find_one({'_id': 'about'})
        privacy = DynamicFiles.find_one({'_id': 'privacy'})
        termsOfService = DynamicFiles.find_one({'_id': 'termsOfService'})
        QandA = DynamicFiles.find_one({'_id': 'QandA'})
        introVideo = DynamicFiles.find_one({'_id': 'introVideo'})
        pathName = self.get_argument('pathName', '')
        if not pathName:
            pathName = 'none'
        else:
            pathName = '/' + pathName
        self.render('index.html', account=self.current_user, pathName=pathName, banner=banner, about=about, privacy=privacy, termsOfService=termsOfService, QandA=QandA, introVideo=introVideo)


class MainPageShow(common.BaseHandler):  # 上一頁功能
    @tornado.web.asynchronous
    def get(self):
        self.render('index.html', account=self.current_user)   
