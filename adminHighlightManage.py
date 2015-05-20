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
        arg1 = self.get_argument('arg1', None)
        if arg1=='add':
            self.render('adminHightlightAdd.html')
        elif arg1=='modify':
            self.render('adminHightlightModify.html')
        else:
            self.render('adminHighlightManage.html')
        
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', None)
        if arg1=='add':
            highlightAdd(self)
        elif arg1=='modify':
            highlightModify(self)
        else:
            self.redirect('/admin/highlight')

def highlightAdd(heandler):
    pass

def highlightModify(handler):
    pass
