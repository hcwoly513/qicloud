# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminTeacherManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

from bson.objectid import ObjectId
import tornado.web
import common


class TeacherManage(common.BaseHandler):
    """
    Data Model
      _id                  ObjectId  e.g. ObjectId
      teacherName          String    e.g. 黃小明
      teacherInfo          String    e.g. 台北帝國大學 數學系碩士
      specialty            String    e.g. 離散數學
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
            teacher = Teacher.find_one({'_id': ObjectId(teacherId)})
            self.render('adminTeacherModify.html', teacher=teacher)
        elif arg1=='del':
            teacherId = self.get_argument('teacherId')
            Teacher.delete_one({'_id': ObjectId(teacherId)})
            self.redirect('/')
    
    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Teacher = db.Teacher
        if arg1=='add':
            teacherName = self.get_argument('teacherName')
            teacherInfo = self.get_argument('teacherInfo')
            specialty = self.get_argument('specialty')
            Teacher.insert_one({'teacherName': teacherName, 'teacherInfo': teacherInfo, 'specialty': specialty})
            self.redirect('/')
        elif arg1=='modify':
            teacherId = self.get_argument('teacherId')
            teacherName = self.get_argument('teacherName')
            teacherInfo = self.get_argument('teacherInfo')
            specialty = self.get_argument('specialty')
            Teacher.update(
                {'_id': ObjectId(teacherId)},
                {'$set': {'teacherName': teacherName,
                          'teacherInfo': teacherInfo,
                          'specialty': specialty}})
            self.redirect('/')
        elif arg1=='del':
            pass