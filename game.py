# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class Game(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        pass
    
    def post(self):
        pass