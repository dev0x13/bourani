# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
import Tools
import os
import sys

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index(uid):
    query = "SELECT * FROM departments WHERE institute = %s ORDER BY name ASC"
    data = (uid)
    db.execute(query, data)
    departments = db.fetchall()
    return render_template("departments.html", departments = departments)
