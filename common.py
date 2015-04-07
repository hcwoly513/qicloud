# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler


class BaseHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get_current_user(self):
        return self.get_secure_cookie('account')
    
