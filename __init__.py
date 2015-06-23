# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, session, url_for, request, Flask
from flask.ext.login import logout_user, LoginManager, current_user, login_required
from db_connection import db
from config import DefaultConfig
from components import Institutes, User, Departments, Courses, Info, Subjects
from components import Files, Admin, Comments, Tools

app = Flask(__name__)
app.config.from_object(DefaultConfig)

# Flask-login parameters
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(uid):
    query = "SELECT * FROM administration WHERE uid = %s"
    data = (uid)
    if db.execute(query, data):
        (row,) = db.fetchall()
        return User.User(row)
    else:
        return None

# Methods for actions
methods = ["GET", "POST"]

# Common routes

@app.route("/login", methods = methods)
def login():
    return Admin.auth()

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/")
def index():
    return Institutes.index()

@app.route("/info")
def info():
    return Info.index()

@login_required
@app.route("/delete/<entity>/<uid>")
def delete(entity, uid):
    return Admin.delete(entity, uid)

# Abstraction levels

@app.route("/institute/<uid>")
@Tools.exists("institutes", "uid")
def institute(uid):
    return Departments.index(uid = uid)

@app.route("/departments/<department>")
@Tools.exists("departments", "department")
def department(department):
    return Courses.index(department = department)

@app.route("/departments/<department>/<course>", methods = methods)
@Tools.exists("departments", "department")
def subjects(department, course):
    return Subjects.index(course, department = department)

@app.route("/subject/<uid>", methods = methods)
@Tools.exists("subjects", "uid")
def subject(uid):
    return Files.index(subject = uid)

@login_required
@app.route("/subjects/delete/<uid>", methods = methods)
@Tools.exists("subjects", "uid")
def delete_subject(uid):
    return Subjects.delete(uid = uid)

@app.route("/file/<uid>", methods = methods)
@Tools.exists("files", "uid")
def file(uid):
    return Files.show_file(uid = uid)

@app.route("/file/<file_uid>/comment", methods = methods)
@Tools.exists("files", "file_uid")
def add_comment(file_uid):
    return Comments.add(file_uid = file_uid)

@login_required
@app.route("/comments/delete/<uid>", methods = methods)
@Tools.exists("comments", "uid")
def delete_comment(uid):
    return Comments.delete(uid = uid)

@app.route("/download/<uid>")
@Tools.exists("files", "uid")
def download_file(uid):
    return Files.download(uid = uid)

@app.route("/search", methods = methods)
def search_file():
    return Files.search()

@login_required
@app.route("/files/delete/<uid>", methods = methods)
@Tools.exists("files", "uid")
def delete_file(uid):
    return Files.delete(uid = uid)

if __name__ == "__main__":
    app.run()
