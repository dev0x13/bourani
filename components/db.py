# -*- coding: utf-8 -*-

import MySQLdb

class Db(object):
    def __init__(self, host, user, password, db):
        self.db = MySQLdb.connect(host, user, password, db, charset = "utf8")
        self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

    def execute(self, query, data = None):
        if not data:
            data = []
        number_of_rows = self.cursor.execute(query, data)
        self.db.commit()
        return number_of_rows

    def fetchall(self):
        return self.cursor.fetchall()

    def __del__(self):
        self.db.close()
