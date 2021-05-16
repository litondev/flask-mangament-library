from main import db

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False,index=True)
    password = db.Column(db.Text,nullable=False)
    role = db.Column(db.Enum('admin','user'),default=True,server_default="user")
    photo = db.Column(db.String(50),default=True,server_default="user.png")
    created_at = db.Column(db.DateTime(timezone=True),nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True),nullable=True)
    
    def __init__(self, username, email, password, role = "user", photo = "user.png"):
      self.username = username
      self.email = email
      self.password = password
      self.role = role
      self.photo = photo
 
    def __repr__(self):     
      return '<User username={self.username} email={self.email}  password={self.password} photo={self.photo} role={self.role}>'