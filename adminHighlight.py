# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminHighlightManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

from bson.objectid import ObjectId
import tornado.web
import common


class HighlightManage(common.BaseHandler):
    """
    Data Model
      _id                    ObjectId  e.g. ObjectId
      highlightName          String    e.g. 
      highlightContent       String    e.g. 
      uploadTime             Datetime  e.g. 
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Highlight = db.Highlight
        if arg1=='':
            highlights = Highlight.find({})
            self.render('adminHighlight.html', highlights=highlights)
        elif arg1=='add':
            self.render('adminHighlightAdd.html')
        elif arg1=='modify':
            highlightId = str(self.get_argument('highlightId', ''))
            highlight = Highlight.find_one({'_id': ObjectId(highlightId)})
            self.render('adminHighlightModify.html', highlight=highlight)

    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Highlight = db.Highlight
        if arg1=='add':
            title = self.get_argument('title')
            uploadTime = common.now()
            content = self.get_argument('content')
            Highlight.insert({'title': title, 'uploadTime': uploadTime, 'content': content})
            self.redirect('/')
        elif arg1=='modify':
            highlightId = self.get_argument('highlightId')
            title = self.get_argument('title')
            content = self.get_argument('content')
            Highlight.update(
                {'_id': ObjectId(highlightId)},
                {'$set': {'title': title,
                          'content': content}})
            self.redirect('/')
        elif arg1=='del':
            pass
            