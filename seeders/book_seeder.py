class BookSeeder():
	def run(self,db,Book):
		db.session.add(Book('name'))
		db.session.commit()