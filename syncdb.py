# -*- coding: utf-8
#!/usr/bin/env python3.4
# Name: main.py
# Author: Chen-Wei Hung
# Created Time: 2015-03-23
# Updated Time: 2015-03-23
# Copyright:   (c) PaulX 2015

import peewe
from models import *

def syncdb():
    db.create_tables([DynamicFiles, Member, CourseType, Unit,
                      Course, CourseDiscussion, Topic, ])
    
syncdb()