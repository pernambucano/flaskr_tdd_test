from app import db

class Manifesto(db.Model):
    
    __tablename__ = "manifesto"

    post_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    text = db.Column(db.String, nullable = False)

    def __init__(self, title, text):
        self.title = title
        self.text = text
    
    def __repr__(self):
        return '<title {}>'.format(self.body)

