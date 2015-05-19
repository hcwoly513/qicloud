# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name:         main.py
# Author:       Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright © PaulX 2015

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import admin
import adminCourseManage
import adminExamManage
import adminGameManage
import adminHighlightManage
import adminMainPageManage
import adminMemberManage
import adminTeacherManage
import adminUnitManage
import common
import forget
import login
import showCourse
import showExam
import showGame
import showHighlight
import showMember
import showTeacher
import signin
import views

define('cmd', default='runserver', metavar='runserver|syncdb')
define('port', default=8000, help='run on the given port', type=int)


class Application(tornado.web.Application):
    # Application initialize settings.
    def __init__(self):
        handlers = [
            (r'/admin',           admin.Admin),
            (r'/admin/course',    adminCourseManage.CourseManage),
            (r'/admin/exam',      adminExamManage.ExamManage),
            (r'/admin/game',      adminGameManage.GameManage),
            (r'/admin/highlight', adminHighlightManage.HighlightManage),
            (r'/admin/mainPage',  adminMainPageManage.MainPageManage),
            (r'/admin/member',    adminMemberManage.MemberManage),
            (r'/admin/teacher',   adminTeacherManage.TeacherManage),
            (r'/admin/unit',      adminUnitManage.UnitManage),
            (r'/forget',          forget.Forget),
            (r'/login',           login.Login),
            (r'/logout',          login.Logout),
            (r'/course',          showCourse.Course),
            (r'/exam',            showExam.Exam),
            (r'/highlight',       showHighlight.Highlight),
            (r'/member',          showMember.Member),
            (r'/signin',          signin.Signin),
            (r'/serve/([^/]+)?', common.ServeHandler),
            (r'/mainPageShow',   views.MainPageShow),
            (r'/.*',             views.MainHandler), # This line has to be at the last line.
            ]
        settings = {
            'template_path' : os.path.join(common.BASEPATH, 'templates'),
            'static_path' :   os.path.join(common.BASEPATH, 'static'),
            'cookie_secret':  '%8E=zdmsoSe)D4AM$V!cGXf&r(#YLWl_t05ikpPngqK2B^7QHOZR*aj6TJyF1UuI',
            'xsrf_cookies':   True,
            'login_url':      '/login',
            'autoreload':     True,
            'debug' :         True,}
        self.db, self.fs = common.dbConnection()
        super(Application, self).__init__(handlers, **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    if options.cmd == 'runserver':
        main()