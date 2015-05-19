# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name:         views.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:    (c) PaulX 2015

import tornado.web
import common

class Teacher(common.BaseHandler):
    def get(self):
        arg1 = self.get_argument('arg1', None)
        
    
    def post(self):
        arg1 = self.get_argument('arg1', None)