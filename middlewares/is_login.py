from flask import g,request,session,redirect
from functools import wraps

def is_login(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		if session.get("user") is None:
			return redirect("/signin")
		return f(*args,**kwargs)
	return decorated_function