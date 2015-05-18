# -*- coding: utf-8
#!/usr/bin/env python
# Name:         member.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:    © PaulX 2015

import tornado.web


class Member(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('member.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass