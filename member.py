# -*- coding: utf-8
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
from models import *

class Member(tornado.web.RequestHandler):
    def get(self):
        self.render('member.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass