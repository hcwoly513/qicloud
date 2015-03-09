# -*- coding: utf-8
#!/usr/bin/env python

def inserted(result, error):
    if error:
        raise error
    db.users.find_one({'name': 'Ben'}, callback=found_one)

def found_one(result, error):
    if error:
        raise error
    print(result)