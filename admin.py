# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common


class Admin(common.BaseHandler):
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        
    
    def post(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')

