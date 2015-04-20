# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: game.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import tornado.web
import common
from models import *


class Game(tornado.web.RequestHandler):
    def get(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        self.render('game.html')
    
    def post(self):
        arg1 = self.get_arguments('arg1')
        arg2 = self.get_arguments('arg2')
        self.render('game.html')