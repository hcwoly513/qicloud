# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         adminCourseManage.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import random
import uuid
import tornado.web
import common


class CourseManage(common.BaseHandler):
    """
    Data Model
      _id                 String    e.g. UUID4亂數
      courseName          String    e.g. 國三數學
      courseInfo          String    e.g. 國三數學第三章
      courseType          String    e.g. 數學
      courseVideo         Blob      e.g. Gridfs File Name
      courseTeacher       String    e.g. 黃小明
      uploadTime          Datetime  e.g. 2015-05-31T15:17:53.080Z
    """
    @tornado.web.asynchronous
    def get(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        Course = db.Course
        if arg1=='':
            courses = Course.find({})
            self.render('adminCourse.html', courses=courses)
        elif arg1=='add':
            self.render('adminCourseAdd.html')
        elif arg1=='modify':
            courseId = self.get_argument('courseId')
            course = Course.find_one({'_id': courseId})
            self.render('adminCourseModify.html', course=course)

    @tornado.web.asynchronous
    def post(self):
        account = self.current_user
        if account != 'admin':
            self.redirect('/')
        arg1 = self.get_argument('arg1', '')
        db = common.dbConnection()
        fs = common.gridfsConnection()
        Course = db.Course        
        if arg1=='':
            pass
        elif arg1=='add':
            rnId = ''.join(str(uuid.uuid4()).split('-'))
            courseName = self.get_argument('courseName')
            courseType = self.get_argument('courseType')
            courseTeacher = self.get_argument('courseTeacher')
            courseInfo = self.get_argument('courseInfo')
            file = self.request.files['courseVideo'][0]
            rnFile = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(64))
            fs.put(file['body'], content_type=file['content_type'], filename=rnFile)
            Course.insert({
                '_id': rnId,
                'courseName'   : courseName,
                'courseType'   : courseType,
                'courseTeacher': courseTeacher,
                'courseInfo'   : courseInfo,
                'courseVideo'  : rnFile,
                'uploadTime'   : common.now()})
            self.redirect('/admin')
        elif arg1=='modify':
            courseId = self.get_argument('courseId', '')
            courseName = self.get_argument('courseName', '')
            courseType = self.get_argument('courseType', '')
            courseTeacher = self.get_argument('courseTeacher', '')
            courseInfo = self.get_argument('courseInfo', '')
            file = self.request.files['courseVideo'][0]
            rnFile = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(64))
            fs.put(file['body'], content_type=file['content_type'], filename=rnFile)
            Course.update({
                '_id': ObjectId(courseId)},
                {'$set': {'courseName'   : courseName,
                          'courseType'   : courseType,
                          'courseTeacher': courseTeacher,
                          'courseInfo'   : courseInfo,
                          'courseVideo'  : rnFile}})
            self.redirect('/admin')
            