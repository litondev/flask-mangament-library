from main import db

class GuestBook(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    description = db.Column(db.Text,nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True),nullable=True)
    user = db.relationship('User')
    
    def __init__(self, user_id, description = None):
      self.user_id = user_id
      self.description = description
 
    def __repr__(self):     
      return '<GuestBook user_id={self.user_id} description={self.description}>'