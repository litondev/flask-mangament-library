from seeders.user_seeder import UserSeeder
from seeders.book_seeder import BookSeeder
from seeders.guest_book_seeder import GuestBookSeeder

def RunSeeder(db,**model):
	user_seeder = UserSeeder()
	user_seeder.run(db,model['user'])

	guest_book_seeder = GuestBookSeeder()
	guest_book_seeder.run(db,model['guest_book'])

	book_seeder = BookSeeder()
	book_seeder.run(db,model['book'])