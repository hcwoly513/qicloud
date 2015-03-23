# -*- coding: utf-8
#!/usr/bin/env python
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
import motor
define('port', default=8000, help='run on the given port', type=int)
qiclouddb = motor.MotorClient('mongodb://qicloud:asd56123zxc@localhost', 27017).qicloud

class Application(tornado.web.Application):
    # Application initialize settings.
    def __init__(self):
        handlers = [
            #(r'/member', ),
            #(r'/login', account.Login),
            (r'/', MainHandler),]
        settings = {
            'db' : qiclouddb,
            'template_path' : os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path' : os.path.join(os.path.dirname(__file__), 'static'),
            'autoreload': True,
            'debug' : True,}
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()