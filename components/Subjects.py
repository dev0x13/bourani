# -*- coding: utf-8 -*-

from flask import render_template
import os
import sys
from Forms import SubjectForm

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index(department, course):
    form = SubjectForm()
    if form.validate_on_submit():
        query = """INSERT INTO subjects(name, department, course, active)
                               VALUES(%s, %s, %s, %s)"""
        data = (form.name.data, department, course, 1)
        db.execute(query, data)
    query = """SELECT * FROM subjects WHERE
                 department = %s AND course = %s AND active = 1
                 ORDER BY name ASC"""
    data = (department, course)
    db.execute(query, data)
    subjects = db.fetchall()
    return render_template("subjects.html", subjects = subjects, form = form)
