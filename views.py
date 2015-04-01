# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.ioloop
import tornado.web
import torndsession.sessionhandler
    
class MainHandler(torndsession.sessionhandler.SessionBaseHandler):
    def get(self):
        self.render('index.html')
    
