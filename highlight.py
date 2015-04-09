# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common

class Highlight(common.BaseHandler):
    def get(self):
        pass
    
    @tornado.web.asynchronous
    def post(self):
        pass