from app import app
from flask import request,flash,redirect,session
from validations.user.signin_validation import SigninValidation
from models import User

class Auth:
	@app.route("/signin",methods=["POST"])
	def user_auth_signin_actions():
		form = SigninValidation(request.form)

		if not form.validate():
			flash({
				"status" : "failed",
				"message" : form.errors[list(form.errors.keys())[0]][0]
			})
			return redirect("/")

		user = User.query.filter_by(email=request.form['email']).first()

		if user == None:
			return redirect("/")

		session["user"] = user.id
		return redirect("/user")

	@app.route("/signup",methods=["POST"])
	def user_auth_signup_actions():
		return "post signup"
