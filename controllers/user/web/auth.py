from app import app
from flask import render_template,g,request,session,redirect
from functools import wraps

def login_required(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		if session.get("user") is None:
			return redirect("/signin")
		return f(*args,**kwargs)
	return decorated_function

class Auth:
	@app.route("/")
	@app.route("/signin")
	def user_auth_signin():
		return render_template('user/signin.html')

	@app.route("/signup")
	@login_required
	def user_auth_signup():
		return "You are login"

	@app.route("/logout")
	@login_required
	def user_auth_logout():
		session.clear()
		return redirect("/")
