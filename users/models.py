from gift_list import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(60))
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
    
    def __repr__(self):
        return "<User %r>" % self.name
    