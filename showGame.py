# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         showGame.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
import common


class Game(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1', None)[0]
        arg2 = self.get_argument('arg2', None)[0]
        self.render('game.html')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account is None:
            self.redirect('/login')
        arg1 = self.get_argument('arg1')[0]
        arg2 = self.get_argument('arg2')[0]
        self.render('game.html')