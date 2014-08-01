from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, FileField
from wtforms.validators import Required

class SubjectForm(Form):
    name = TextField("name", validators = [Required()])
    recaptcha = RecaptchaField()

class FileForm(Form):
    file_to_upload = FileField("file_to_upload", validators = [Required()])
    description = TextAreaField("description", validators = [Required()])
    #recaptcha = RecaptchaField()
