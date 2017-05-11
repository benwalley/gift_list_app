from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    name = StringField("Name", [validators.Required()])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message = "Passwords must match"),
        validators.Length(max = 80)
        ])
    confirm = PasswordField('Repeat Password')
    
class LoginForm(Form):
    name = StringField("Name", [
        validators.Required(),
        validators.Length(max=80)
        ])
    password = PasswordField("Password", [
        validators.Required(),
        validators.Length(min=4, max=80)
        ])