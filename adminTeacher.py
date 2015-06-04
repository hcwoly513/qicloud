# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminTeacherManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import uuid
import tornado.web
import common


class TeacherManage(common.BaseHandler):
    """
    Data Model
      _id                  String  e.g. UUID4亂數
      teacherName          String  e.g. 黃小明
      teacherInfo          String  e.g. 台北帝國大學 數學系碩士
      specialty            String  e.g. 離散數學
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Teacher = db.Teacher
        if arg1=='':
            teachers = Teacher.find()
            self.render('adminTeacher.html', teachers=teachers)
        elif arg1=='add':
            self.render('adminTeacherAdd.html')
        elif arg1=='modify':
            teacherId = self.get_argument('teacherId')
            teacher = Teacher.find_one({'_id': teacherId})
            self.render('adminTeacherModify.html', teacher=teacher)
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Teacher = db.Teacher
        if arg1=='add':
            rnId = ''.join(str(uuid.uuid4()).split('-'))
            teacherName = self.get_argument('teacherName')
            teacherInfo = self.get_argument('teacherInfo')
            specialty = self.get_argument('specialty')
            Teacher.insert_one({'_id': rnId, 'teacherName': teacherName, 'teacherInfo': teacherInfo, 'specialty': specialty})
            self.redirect('/')
        elif arg1=='modify':
            teacherId = self.get_argument('teacherId')
            teacherName = self.get_argument('teacherName')
            teacherInfo = self.get_argument('teacherInfo')
            specialty = self.get_argument('specialty')
            Teacher.update(
                {'_id': teacherId},
                {'$set': {'teacherName': teacherName,
                          'teacherInfo': teacherInfo,
                          'specialty': specialty}})
            self.redirect('/')
        elif arg1=='del':
            pass