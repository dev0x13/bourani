# -*- coding: utf-8 -*-

from flask import render_template

def index(department):
    return render_template("courses.html", department = department)
