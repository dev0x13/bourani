# -*- coding: utf-8 -*-

import re

def format_date(date):
    regexp = "^(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2}):(\d{2})$"
    match = re.match(regexp, str(date))
    if match:
        matches = match.groups()
        return "{0}.{1}.{2} {3}:{4}:{5}".format(matches[2], matches[1],
                                                matches[0], matches[3],
                                                matches[4], matches[5])
    return "0000-00-00 00:00:00"
