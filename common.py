# -*- coding: utf-8
#!/usr/bin/env python3.4

import tornado.web
import tornado.ioloop
import torndsession

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')
    
def checkSession():
    pass