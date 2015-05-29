# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminMemberManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class MemberManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        arg2 = self.get_argument('arg2', '')
        Member = self.application.db.Member
        if arg1=='':
            members = Member.find({})
            self.render('adminMember.html', members=members)
        if arg1=='add':
            self.render('adminMemberAdd.html')
        elif arg1=='modify':
            memberId = self.get_argument('memberId', '')
            member = Member.find_one({'_id': memberId})
            self.render('adminMemberModify.html', member=member)
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        arg2 = self.get_argument('arg2', '')
        Member = self.application.db.Member
        if arg1=='add':
            account = self.get_argument('account', '')
            nickname = self.get_argument('nickname', '')
            password = self.get_argument('password', '')
            email = self.get_argument('email', '')
            if Member.find_one({'_id': account}):
                self.write('FALSE')
            else:
                Member.insert_one({
                    '_id': account,
                    'account': account,
                    'nickname': nickname,
                    'password': password,
                    'email': email})
        elif arg1=='modify':
            account = self.get_argument('account', '')
            pass