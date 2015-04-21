# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
# Name: syncdb.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

from __future__ import absolute_import, division, print_function, with_statement

import peewee
import common
from models import *

def create_tables():
    db.connect()
    db.create_tables([
        Announcements, DynamicFiles, Member, Course,
        Teacher, CourseType, Unit, CourseDiscussion,
        Topic, Message, Response, Introduction, CourseSurvey,
        Highlight])
    
if __name__ == '__main__':
    create_tables()