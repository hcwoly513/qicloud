# -*- coding: utf-8
#!/usr/bin/env python
# Name:         forget.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class Forget(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        arg1 = self.get_argument('arg1', '')
        if arg1=='getPassword':
            self.render('getPassword.html', errorMessage='')
        else:
            return
    
    @tornado.web.asynchronous
    def post(self):
        arg1 = self.get_argument('arg1', '')
        if arg1=='getPassword':
            account = self.get_argument('account', '')
            email = self.get_argument('email', '')
            if not account or not email:
                self.render('getPassword', errorMessage='請輸入帳號或密碼！')
            
        
        