# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, session, url_for, request, Flask
from flask.ext.login import logout_user, LoginManager, current_user, login_required
from db_connection import db
from config import DefaultConfig
from components import Institutes, User, Departments, Courses, Info, Subjects, Files

app = Flask(__name__)
app.config.from_object(DefaultConfig)

# Flask-login parameters
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = "login"

#@login_manager.user_loader
#def load_user(uid):
    #query = "SELECT * FROM administration WHERE uid = %s"
    #data = (uid)
    #db.execute(query, data)
    #(row,) = db.cursor.fetchall()
    #return User.User(row)

# Methods for actions
methods = ["GET", "POST"]

@app.route("/")
#@login_required
def index():
    return Institutes.index()

@app.route("/info")
def info():
    return Info.index()

@app.route("/institute/<uid>")
def institute(uid):
    return Departments.index(uid)

@app.route("/departments/<uid>")
def department(uid):
    return Courses.index(uid)

@app.route("/subjects/<department>/<course>", methods = methods)
def subjects(department, course):
    return Subjects.index(department, course)

@app.route("/subject/<uid>")
def subject(uid):
    return Files.index(subject)

if __name__ == "__main__":
    app.run()
