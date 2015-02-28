# -*- coding: utf-8
#!/usr/bin/env python

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
#import account

from tornado.options import define, options
from pymongo.member import Member
define('port', default=80, help='run on the given port', type=int)

class Application(tornado.web.Application):
    # Application initialize settings.
    def __init__(self):
        handlers = [
            #(r'/member', ),
            #(r'/login', account.Login),
            (r'/', MainHandler),]
        settings = {
            'template_path' : os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path' : os.path.join(os.path.dirname(__file__), 'static'),
            'autoreload': True,
            'debug' : True,}
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()