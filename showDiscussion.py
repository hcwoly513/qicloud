# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         discussion.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class Discussion(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        pass
    
    @tornado.web.asynchronous
    def post(self):
        pass