# -*- coding: utf-8 -*-

from flask import render_template, redirect
import os
import sys

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index():
    query = "SELECT * FROM institutes"
    db.execute(query)
    institutes = db.fetchall()
    return render_template("institutes.html", institutes = institutes)

def show_institute(uid):
    query = "SELECT uid FROM departments WHERE institute = %s"
    data = (uid)
    departments = db.execute(query)
    return render_template("departments.html", departments = departments)
