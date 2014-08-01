from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField
from wtforms.validators import Required

class SubjectForm(Form):
    name = TextField("name", validators = [Required()])
    recaptcha = RecaptchaField()
