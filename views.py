# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.ioloop
import tornado.web
import common

    
class MainHandler(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        cookie = self.get_secure_cookie('count')
        count = int(cookie) + 1 if cookie else 1
        countString = '1 time' if count == 1 else 1
        self.set_secure_cookie('count', str(count))
        self.render('index.html', count=count)
    

