# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: views.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

from __future__ import absolute_import, division, print_function, with_statement

import tornado.web
import common
from models import *


class MainHandler(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_argument('arg1', None)
        arg2 = self.get_argument('arg2', None)
        pathName = self.get_argument('pathName', None)
        if not pathName:
            pathName = 'none'
        else:
            pathName = '/' + pathName        
        self.render('index.html', account=self.current_user, arg1=arg1, arg2=arg2, pathName = pathName)


class MainPageShow(common.BaseHandler):
    def get(self):
        self.render('index.html', account=self.current_user)   
