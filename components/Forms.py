# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, FileField, PasswordField
from wtforms.validators import Required

# TODO: очистка форм
# TODO: CSRF

class SubjectForm(Form):
    name = TextField("name", validators = [Required()])
    recaptcha = RecaptchaField()

class FileForm(Form):
    file_to_upload = FileField("file_to_upload", validators = [Required()])
    description = TextAreaField("description", validators = [Required()])
    recaptcha = RecaptchaField()

class LoginForm(Form):
    username = TextField("username", validators = [Required()])
    password = PasswordField("password", validators = [Required()])

class CommentForm(Form):
    username = TextField("username")
    text = TextAreaField("text", validators = [Required()])
    recaptcha = RecaptchaField()
