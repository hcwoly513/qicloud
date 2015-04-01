# -*- coding: utf-8
#!/usr/bin/env python3.4

import tornado.ioloop
import tornado.web
import motor


class Login(common.BaseHandler):
    def get(self):
        self.render('login.html') 
    
    def post(self):
        username = self.get_argument('username')
        self.set_secure_cookie('username', username)
        