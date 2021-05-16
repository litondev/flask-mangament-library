from wtforms import Form,StringField,PasswordField,validators

class SigninValidation(Form):
	email = StringField('Email',[
		validators.Length(min=6,max=35)
	])

	password = PasswordField('Password',[
		validators.DataRequired()
	])