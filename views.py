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
        self.render('index.html', account=self.current_user)
    

