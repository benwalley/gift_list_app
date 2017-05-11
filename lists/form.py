from flask_wtf import Form
from wtforms import StringField,validators

class GiftsForm(Form):
    gift = StringField('Gift name', [
        validators.Required(),
        validators.Length(max=80)
        ])
        
    comment = StringField("comments", [
        validators.Length(max=255)
        ])
    
class ExtraForm(Form):
    comment = StringField("Give something else", [
        validators.Length(max=255)
        ])