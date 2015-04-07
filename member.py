# -*- coding: utf-8
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.ioloop
import tornado.web
import motorengine

class Member(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        pass
    
    def post(self):
        pass