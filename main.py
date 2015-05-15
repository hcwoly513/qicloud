# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import admin
import common
import course
import exam
import forget
import highlight
import login
import member
#import models
import signin
import views

define('cmd', default='runserver', metavar='runserver|syncdb')
define('port', default=8000, help='run on the given port', type=int)


class Application(tornado.web.Application):
    # Application initialize settings.
    def __init__(self):
        handlers = [
            (r'/admin', admin.Admin),
            (r'/course', course.Course),
            (r'/exam', exam.Exam),
            (r'/forget', forget.Forget),
            (r'/highlight', highlight.Highlight),
            (r'/login', login.Login),
            (r'/logout', login.Logout),
            (r'/member', member.Member),
            (r'/signin', signin.Signin),
            (r'/serve/([^/]+)?', common.ServeHandler),
            (r'/mainPageShow', views.MainPageShow),
            (r'/.*', views.MainHandler),         # This line has to be at the last line.
            ]
        settings = {
            'template_path' : os.path.join(common.BASEPATH, 'templates'),
            'static_path' : os.path.join(common.BASEPATH, 'static'),
            'cookie_secret': '%8E=zdmsoSe)D4AM$V!cGXf&r(#YLWl_t05ikpPngqK2B^7QHOZR*aj6TJyF1UuI',
            'xsrf_cookies': True,
            'login_url': '/login',
            'autoreload': True,
            'debug' : True,}
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