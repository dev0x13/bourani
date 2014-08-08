# -*- coding: utf-8 -*-

from flask import redirect, url_for
from functools import wraps
import re
import os
import sys

sys.path.append(os.path.abspath(".."))
from db_connection import db

def format_date(date):
    regexp = "^(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2}):(\d{2})$"
    match = re.match(regexp, str(date))
    if match:
        matches = match.groups()
        return "{0}.{1}.{2} {3}:{4}:{5}".format(matches[2], matches[1],
                                                matches[0], matches[3],
                                                matches[4], matches[5])
    return "0000-00-00 00:00:00"

def exists(table, keyword):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if kwargs:
                query = "SELECT uid FROM {0} WHERE uid = %s AND active = 1".format(table)
                data = (kwargs[keyword])
                result = db.execute(query, data)
                if result:
                    return function(*args, **kwargs)
            return redirect(url_for("index"))
        return wrapper
    return decorator
