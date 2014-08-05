# -*- coding: utf-8 -*-

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

def exists(table, uid):
    query = "SELECT uid FROM {0} WHERE uid = %s".format(table)
    data = (uid)
    result = db.execute(query, data)
    return True if result else False
