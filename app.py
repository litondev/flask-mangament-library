from main import db,app
from models import User,GuestBook,Book
from seeders import RunSeeder
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
import sys

Migrate(app, db)
FlaskSeeder(app,db)

# Seeder
if len(sys.argv) == 3:
	if sys.argv[1] == "seed" and sys.argv[2] == "run":
		RunSeeder(db,user=User,guest_book=GuestBook,book=Book)

# import views from flaskr
import views

if __name__ == "__main__":
    app.run()