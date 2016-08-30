# -*- coding: utf-8 -*-
# Georgiy Manuilov (dev@hl.ru), 2014

from flask import render_template, redirect, url_for
from flask.ext.login import login_user, current_user
from werkzeug.security import check_password_hash
from .User import User
from .Forms import LoginForm, AdminForm
import Tools
import sys
import os

sys.path.append(os.path.abspath(".."))
from db_connection import db

def auth():
    form = LoginForm()
    if form.validate_on_submit():
        query = "SELECT * FROM administration WHERE username = %s"
        data = (form.username.data)
        number_of_rows = db.execute(query, data)
        if number_of_rows != 0:
            (row,) = db.fetchall()
            if check_password_hash(row["password"], form.password.data):
                login_user(User(row))
            return redirect(url_for("index"))
    return render_template("login.html", form = form)

def delete(table, uid):
    query = "SHOW TABLES LIKE %s"
    data = (table)
    existence = db.execute(query, data)
    if existence:
        query = "SELECT uid FROM {0} WHERE uid = %s".format(table)
        data = (uid)
        result = db.execute(query, data)
        if result:
            form = AdminForm()
            action = "/{0}/delete/{1}".format(table, uid)
            return render_template("admin.html", form = form, action = action)
    return redirect(url_for("index"))
