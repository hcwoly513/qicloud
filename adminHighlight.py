# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminHighlightManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class HighlightManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        arg2 = self.get_argument('arg2', '')
        if arg1=='':
            self.render('adminHighlight.html')
        elif arg1=='add':
            self.render('adminHighlightAdd.html')
        elif arg1=='modify':
            self.render('adminHighlightModify.html')

    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        arg2 = self.get_argument('arg2', '')
        if arg1=='':
            pass
        elif arg1=='add':
            highlightAdd(self)
        elif arg1=='modify':
            pass

def highlightAdd(handler):
    title = handler.get_argument('title', None)
    uploadTime = common.now()
    content = handler.get_argument('content', None)
    highlight = handler.application.db.Highlight
    highlight.insert({'title': title, 'uploadTime': uploadTime, 'content': content})
    handler.redirect('/admin')

def highlightModify(handler):
    pass
