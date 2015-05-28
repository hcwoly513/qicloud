# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminUnitManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class UnitManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        Unit = self.application.db.Unit
        self.render('adminUnit.html')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        Unit = self.application.db.Unit
        if arg1=='add':
            pass
        elif arg1=='modify':
            pass
        elif arg=='del':
            pass
        
def unitAdd(handler):
    pass

def unitModify(handler):
    pass