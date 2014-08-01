# -*- coding: utf-8 -*-

from flask import render_template

def index(uid):
    return render_template("courses.html", department = uid)
