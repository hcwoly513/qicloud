# -*- coding: utf-8
#!/usr/bin/env python
# Name: forget.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
from models import *


class Forget(common.BaseHandler):
    def get(self):
        arg1 = self.get_argument('arg1', None)
        arg1 = self.get_argument('arg2', None)
        self.render('forgetPassword.html', errorMessage='')
    
    def post(self):
        pass