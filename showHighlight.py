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
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Highlight = db.Highlight
        if arg1=='':
            highlights = Highlight.find()
            self.render('highlightShow.html', highlights=highlights)
        elif arg1=='showOne':
            highlightId = self.get_argument('highlightId', '')
            highlight = Highlight.find_one({'_id': highlightId})
            self.render('highlightShowOne.html', highlight=highlight)