# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminMemberManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class MemberManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        if arg1=='add':
            self.render('adminMemberAdd.html')
        elif arg1=='modify':
            self.render('adminMemberModify.html')
        else:
            members = self.application.db.Member.find({})
            self.render('adminMember.html', members=members)
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        if arg1=='add':
            pass
        elif arg1=='modify':
            pass
