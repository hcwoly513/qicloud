# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name:         adminGameManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import tornado.web
from bson.objectid import ObjectId
import common


class GameManage(common.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        Game = self.application.db.Game
        if arg1=='':
            games = Game.find()
            self.render('adminGame.html', games=games)
        elif arg1=='add':
            self.render('adminGameAdd.html')
        elif arg1=='modify':
            self.render('adminGameModify.html')

    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        Game = self.application.db.Game
        if arg1=='add':
            gameName = self.get_argument('gameName', '')
            
        elif arg1=='modify':
            gameModify(self)