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
        db = self.application.db
        
        arg1 = self.get_argument('arg1', '')
        if arg1=='':
            highlights = db.Highlight.find({})
            self.render('highlightShow.html', highlights=highlights)
        elif arg1=='show':
            highlightId = self.get_argument('highlightId', '')
            highlight = db.Highlight.find_one({'_id': highlightId})
            self.render('')
        
    
    @tornado.web.asynchronous
    def post(self):
        pass