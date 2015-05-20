# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name:         showHighlight.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class Highlight(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        highlight = self.application.db.Highlight
        self.render('highlightShow.html')
    
    @tornado.web.asynchronous
    def post(self):
        pass