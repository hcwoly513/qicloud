# -*- coding: utf-8
#!/usr/bin/env python
# Name:         showMember.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class Member(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('member.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass