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
    """
    Data Model
      _id               String    e.g. UUID4亂數
      account           String    e.g. 使用者帳戶。
      content           String    e.g. 討論內容。
      title             String    e.g. 討論標題。
      postTime          Datatime  e.g. 2015-05-31T15:17:53.080Z
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if not account == 'admin':
            self.redirect('/')
        db = common.dbConnection()
        fs = common.gridfsConnection()
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if not account == 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        fs = common.gridfsConnection()