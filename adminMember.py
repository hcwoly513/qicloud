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
        Member = self.application.db.Member
        if arg1=='':
            members = Member.find({})
            self.render('adminMember.html', members=members)
        if arg1=='add':
            self.render('adminMemberAdd.html')
        elif arg1=='modify':
            self.render('adminMemberModify.html')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        Member = self.application.db.Member
        if arg1=='add':
            memberAdd(self)
        elif arg1=='modify':
            memberModify(self)

def memberAdd(handler):
    pass

def memberModify(handler):
    pass