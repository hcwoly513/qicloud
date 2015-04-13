# -*- coding: utf-8
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common


class Signin(common.BaseHandler):
    def get(self):
        arg1 = get_arguments('arg1')
        self.render('signin.html')
    
    def post(self):
        account = self.get_arguments('account')
        password = self.get_arguments('password')
        passwordSecond = self.get_arguments('passwordSecond')
        image = self.get_arguments('image')
        email = self.get_arguments('email')
        nickname = self.get_arguments('nickname')
        country = self.get_arguments('country')