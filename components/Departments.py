# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, g, send_file, abort
import os
import sys

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index():
    query = "SELECT uid FROM departments"
    institutes = db.execute(query)
    return render_template("departments.html", departments = departments)
