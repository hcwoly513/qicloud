# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminDiscussionManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import random
import tornado.web
from bson.objectid import ObjectId
import common


class Discussion(common.BaseHandler):
    def get(self):
        account = self.current_user
        if not account == 'admin':
            self.redirect('/')
        db = common.dbConnection()
        fs = common.gridfsConnection()
    
    def post(self):
        account = self.current_user
        if not account == 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        fs = common.gridfsConnection()