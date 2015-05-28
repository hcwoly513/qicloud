# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         admin.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:    © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Admin(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if not account == 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        self.render('admin.html')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if not account == 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')

