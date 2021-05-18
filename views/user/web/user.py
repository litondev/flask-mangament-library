from app import app
from middlewares import is_login

class User:
	@app.route("/user")
	@is_login	
	def user():
		return "hai"

