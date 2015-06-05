# -*- coding: utf-8
#!/usr/bin/env python
# Name:         showMember.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Member(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Member = db.Member
        if arg1=='show':
            memberId = self.get_argument('memberId', '')
            member = Member.find_one({'_id': memberId})
            self.render('member.html', member=member)
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Member = db.Member
        if arg1=='modify':
            account = self.get_argument('account')
            nickname = self.get_argument('nickname')
            password = self.get_argument('password')
            email = self.get_argument('email')
            Member.update(
                {'_id': account},
                {'$set': {'nickname': nickname, 'password': common.encryptPassword(password), 'email': email}})
            self.redirect('/')
            
        