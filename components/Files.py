# -*- coding: utf-8 -*-

from flask import render_template
import os
import sys

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index(subject):
    files = None
    return render_template("files.html", filess = files)
