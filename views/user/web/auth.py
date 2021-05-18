from app import app
from flask import render_template,session,redirect
from middlewares import is_login

class Auth:
	@app.route("/")
	@app.route("/signin")
	def user_auth_signin():
		return render_template('user/signin.html')

	@app.route("/signup")
	def user_auth_signup():
		return "You are login"

	@app.route("/logout")
	@is_login
	def user_auth_logout():
		session.clear()
		return redirect("/")
