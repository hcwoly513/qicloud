# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: exam.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
from models import *


class Exam(common.BaseHandler):
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        self.render('exam.html')
        
    def post(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')