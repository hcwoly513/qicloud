# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: highlight.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

from __future__ import absolute_import, division, print_function, with_statement

import tornado.web
import common
from models import *

class Highlight(common.BaseHandler):
    def get(self):
        self.render('highlight.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass