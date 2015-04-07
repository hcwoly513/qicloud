# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.ioloop
import tornado.web
import motorengine
from motorengine.document import Document

class Account(Document):
    account = StringField(required=True)
    password = StringField(required=True)

class Member(Document):