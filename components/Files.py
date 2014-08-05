# -*- coding: utf-8 -*-

from flask import render_template, send_from_directory, abort, redirect, url_for
from flask.ext.login import current_user
from werkzeug import secure_filename
import os
import sys
import Tools
from Forms import FileForm, AdminForm, CommentForm

sys.path.append(os.path.abspath(".."))
from db_connection import db

def index(subject):
    if Tools.exists("subject", subject):
        form = FileForm()
        if form.validate_on_submit():
            query = """INSERT INTO files(name, filename, description, active, subject, date)
                                   VALUES(%s, %s, %s, 1, %s, NOW())"""
            name = secure_filename(form.file_to_upload.data.filename)
            filename = hashlib.md5(secure_filename(form.file_to_upload.data.filename)).hexdigest()
            data = (name, filename, form.description.data, subject)
            db.execute(query, data)
            path = 'uploads/{0}/'.format(subject)
            if not os.path.exists(path):
                os.mkdir(path, 0777)
            form.file_to_upload.data.save(path + filename)
            form.reset()
        query = "SELECT * FROM files WHERE subject = %s AND active = 1 ORDER BY date DESC"
        data = (subject)
        db.execute(query, data)
        files = db.fetchall()
        return render_template("files.html", files = files, form = form)
    return redirect(url_for("index"))

def download(uid):
    if Tools.exists("files", uid):
        query = "SELECT filename, name, subject FROM files WHERE uid = %s AND active = 1"
        data = (uid)
        result = db.execute(query, data)
        if result:
            (info,) = db.fetchall()
            path = "uploads/{0}/".format(info["subject"])
            if os.path.exists(path + info["filename"]):
                return send_from_directory(path, info["filename"],
                                           attachment_filename = info["name"],
                                           as_attachment = True)
            else:
                abort(404)
    return redirect(url_for("index"))

def show_file(uid):
    if Tools.exists("files", uid):
        query = "SELECT * FROM files WHERE uid = %s AND active = 1"
        data = (uid)
        result = db.execute(query, data)
        if result:
            form = CommentForm()
            (info,) = db.fetchall()
            info["date"] = Tools.format_date(info["date"])
            query = "SELECT * FROM comments WHERE file = %s AND active = 1"
            data = (uid)
            db.execute(query, data)
            comments = db.fetchall()
            for comment in comments:
                comment["date"] = Tools.format_date(comment["date"])
            return render_template("file.html", info = info,
                                   comments = comments, form = form)
    return redirect(url_for("index"))

def delete(uid):
    if Tools.exists("files", uid):
        form = AdminForm()
        if form.validate_on_submit():
            comment = u"-[УДАЛЕНО]-\r\nПричина: {0}\r\nАдминистратор: {1}\r\nВремя: ".format(form.reason.data, current_user.uid)
            query = "UPDATE files SET active = 0, comment = CONCAT(%s, NOW()) WHERE uid = %s"
            data = (comment, uid)
            db.execute(query, data)
        query = "SELECT subject FROM files WHERE uid = %s"
        data = (uid)
        result = db.execute(query, data)
        if result:
            (info,) = db.fetchall()
            return redirect(url_for("subject", uid = info["subject"]))
    return redirect(url_for("index"))
