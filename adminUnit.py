# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminUnitManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import uuid
import tornado.web
import common


class UnitManage(common.BaseHandler):
    """
    Data Model
      _id               String   e.g. 
      unitName          String   e.g. 
      unitInfo          String   e.g. 
      unitType          String   e.g. 
      numCourses        Integer  e.g. 
      teacherId         String   e.g. 
      uploadTime        String   e.g. 
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Unit = db.Unit
        if arg1=='':
            units = Unit.find()
            self.render('adminUnit.html', units=units)
        elif arg1=='add':
            pass
        elif arg1=='modify':
            pass
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Unit = db.Unit
        if arg1=='add':
            rnId = ''.join(str(uuid.uuid4()).split('-'))
        elif arg1=='modify':
            unitId = str(self.get_argument('unitId', ''))
        elif arg=='del':
            pass