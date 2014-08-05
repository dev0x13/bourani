# -*- coding: utf-8 -*-

from flask import render_template, send_from_directory, abort, redirect, url_for
from flask.ext.login import current_user
from werkzeug import secure_filename
import os
import sys
import Tools
from Forms import CommentForm, AdminForm

sys.path.append(os.path.abspath(".."))
from db_connection import db

def add(file_uid):
    if Tools.exists("files", file_uid):
        form = CommentForm()
        if form.validate_on_submit():
            username = u"Аноним" if not form.username.data else form.username.data
            query = """INSERT INTO comments(username, text, active, date, file)
                                   VALUES(%s, %s, 1, NOW(), %s)"""
            data = (username, form.text.data, file_uid)
            db.execute(query, data)
            form.reset()
            data = (uid)
        return redirect(url_for("file", uid = file_uid))
    return redirect(url_for("index"))

def delete(uid):
    if Tools.exists("comments", uid):
        form = AdminForm()
        if form.validate_on_submit():
            comment = u"-[УДАЛЕНО]-\r\nПричина: {0}\r\nАдминистратор: {1}\r\nВремя: ".format(form.reason.data, current_user.uid)
            query = "UPDATE comments SET active = 0, comment = CONCAT(%s, NOW()) WHERE uid = %s"
            data = (comment, uid)
            db.execute(query, data)
        query = "SELECT file FROM comments WHERE uid = %s"
        data = (uid)
        result = db.execute(query, data)
        if result:
            (info,) = db.fetchall()
            return redirect(url_for("file", uid = info["file"]))
    return redirect(url_for("index"))
