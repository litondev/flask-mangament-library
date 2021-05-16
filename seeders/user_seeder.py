class UserSeeder():
	def run(self,db,User):
		db.session.add(User('usernname','email','password'))
		db.session.commit() 