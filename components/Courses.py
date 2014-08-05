# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
import Tools

def index(uid):
    if Tools.exists("departments", uid):
        return render_template("courses.html", department = uid)
    return redirect(url_for("index"))
