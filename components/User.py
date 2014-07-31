# -*- coding: utf-8 -*-

class User:
    lang = "ru"

    def __init__(self, attributes):
        self.uid = attributes["uid"]
        self.username = attributes["username"]
        self.password = attributes["password"]

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.uid)
