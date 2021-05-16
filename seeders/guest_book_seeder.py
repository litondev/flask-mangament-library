class GuestBookSeeder():
	def run(self,db,GuestBook):
		db.session.add(GuestBook(1,'description'))
		db.session.commit()
		
		db.session.add(GuestBook(1))
		db.session.commit()