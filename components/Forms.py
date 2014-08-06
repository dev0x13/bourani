# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, FileField, PasswordField
#from werkzeug.datastructures import MultiDict
from wtforms import validators

# TODO: regenerate CSRF token
#class ReusableForm(Form):
#    def reset(self):
#      blankData = MultiDict([("csrf", self.reset_csrf())])
#      self.process(blankData)

class ReusableForm(Form):
    def reset(self):
      self.process(None)

class SubjectForm(ReusableForm):
    name = TextField("name", [validators.Required(), validators.Length(max = 255)])
    recaptcha = RecaptchaField()

class FileForm(ReusableForm):
    file_to_upload = FileField("file_to_upload", [validators.Required()])
    description = TextAreaField("description", [validators.Required()])
    recaptcha = RecaptchaField()

class LoginForm(ReusableForm):
    username = TextField("username", [validators.Required(), validators.Length(max = 255)])
    password = PasswordField("password", [validators.Required(), validators.Length(max = 255)])

class CommentForm(ReusableForm):
    username = TextField("username", [validators.Length(max = 255)])
    text = TextAreaField("text", [validators.Required()])
    recaptcha = RecaptchaField()

class AdminForm(ReusableForm):
    reason = TextAreaField("reason", [validators.Required()])
    recaptcha = RecaptchaField()

class SearchForm(ReusableForm):
    search_string = TextField("search_string")
