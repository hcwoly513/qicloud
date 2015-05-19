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
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        self.render('forgetPassword.html', errorMessage='')
    
    @tornado.web.asynchronous
    def post(self):
        email = self.get_argument('email', None)
        