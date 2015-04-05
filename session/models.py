# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4

import peewee

db = peewee.SqliteDatabase('session.sqlite3')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class SessionModel(BaseModel):
    pdump = peewee.BlobField()