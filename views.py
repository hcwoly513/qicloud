# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: views.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
from models import *


class MainHandler(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        pathName = self.get_argument('pathName', None)
        if not pathName:
            pathName = 'none'
        else:
            pathName = '/' + pathName        
        self.render('index.html', account=self.current_user, pathName = pathName)


class MainPageShow(common.BaseHandler):  # 上一頁功能
    def get(self):
        self.render('index.html', account=self.current_user)   
