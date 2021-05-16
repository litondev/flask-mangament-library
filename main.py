from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_wtf.csrf import CSRFProtect

load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/testing'

app.secret_key = os.getenv('SECRET_KEY')

csrf = CSRFProtect(app)

db = SQLAlchemy(app)