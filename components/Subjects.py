# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from flask.ext.login import current_user
import os
import sys
from Forms import SubjectForm, AdminForm

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index(department, course):
    form = SubjectForm()
    if form.validate_on_submit():
        query = """INSERT INTO subjects(name, department, course, active)
                               VALUES(%s, %s, %s, %s)"""
        data = (form.name.data, department, course, 1)
        db.execute(query, data)
        form.reset()
    query = """SELECT * FROM subjects WHERE
                 department = %s AND course = %s AND active = 1
               ORDER BY name ASC"""
    data = (department, course)
    db.execute(query, data)
    subjects = db.fetchall()
    return render_template("subjects.html", subjects = subjects, form = form)

def delete(uid):
    form = AdminForm()
    if form.validate_on_submit():
        comment = u"-[УДАЛЕНО]-\r\nПричина: {0}\r\nАдминистратор: {1}\r\nВремя: ".format(form.reason.data, current_user.uid)
        query = "UPDATE subjects SET active = 0, comment = CONCAT(%s, NOW()) WHERE uid = %s"
        data = (comment, uid)
        db.execute(query, data)
        query = "UPDATE files SET active = 0, comment = CONCAT(%s, NOW()) WHERE subject = %s"
        db.execute(query, data)
    query = "SELECT department, course FROM subjects WHERE uid = %s"
    data = (uid)
    result = db.execute(query, data)
    if result:
        (info,) = db.fetchall()
        return redirect(url_for("subjects", department = info["department"], course = info["course"]))
    return redirect(url_for("index"))
