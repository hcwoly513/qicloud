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
define('port', default=8000, help='run on the given port', type=int)
import views, login, member, course, game, exam, highlight, signin

class Application(tornado.web.Application):
    # Application initialize settings.
    def __init__(self):
        handlers = [
            (r'/', views.MainHandler),
            (r'/login', login.Login),
            (r'/login', login.Login),
            (r'/login', login.Login),
            (r'/logout', login.Logout),
            (r'/signin', signin.Signin),
            (r'/member', member.Member),
            (r'/course', course.Course),
            (r'/game', game.Game),
            (r'/exam', exam.Exam),
            (r'/highlight', highlight.Highlight),
            ]
        settings = {
            'template_path' : os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path' : os.path.join(os.path.dirname(__file__), 'static'),
            'cookie_secret': '%8E=zdmsoSe)D4AM$V!cGXf&r(#YLWl_t05ikpPngqK2B^7QHOZR*aj6TJyF1UuI',
            'xsrf_cookies': True,
            'login_url': '/login',
            'autoreload': True,
            'debug' : True,}
        tornado.web.Application.__init__(self, handlers, **settings)
        
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()