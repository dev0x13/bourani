# -*- coding: utf-8 -*-

from flask import render_template, redirect
import os
import sys

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index():
    query = "SELECT * FROM institutes ORDER BY name ASC"
    db.execute(query)
    institutes = db.fetchall()
    return render_template("institutes.html", institutes = institutes)
