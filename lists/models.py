from gift_list import db

class Gifts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gift = db.Column(db.String(80))
    comment = db.Column(db.String(255))
    wanter = db.Column(db.String(80))
    giver = db.Column(db.String(80))
    
    
    def __init__(self, gift, comment, wanter):
        self.gift = gift
        self.comment = comment
        self.wanter = wanter
        
        
        
    def __repr__(self):
        return "<Gifts %r>" % self.gift
        
class Extras(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(80))
    wanter = db.Column(db.String(80))
    giver = db.Column(db.String(80))
    
    def __init__(self, comment, wanter, giver):
        self.comment = comment
        self.wanter = wanter
        self.giver = giver
        
    def __repr__(self):
        return "<comment %r>" % self.comment