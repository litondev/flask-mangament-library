from main import db

class Book(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    status = db.Column(db.Enum('on borrow','off borrow'),default=True,server_default="off borrow")
    created_at = db.Column(db.DateTime(timezone=True),nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True),nullable=True)

    def __init__(self, name, status = 'off borrow'):    
      self.name = name
      self.status = status
 
    def __repr__(self):  
      return '<Book name={self.name} status={self.status}>'