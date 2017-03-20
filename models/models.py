from peewee import *
import datetime

# Load Database
db = SqliteDatabase('database/data.db')

class Users(Model):
	id = PrimaryKeyField()
	email = CharField()
	username = CharField()
	password = CharField()
	receive_updates = CharField(default = "yes")
	role = CharField(default = "user")

	class Meta:
		database = db

class Post(Model):
	id = PrimaryKeyField()
	date = DateTimeField(default = datetime.datetime.now)
	comments = CharField()
	title = CharField()
	img = TextField()
	desc = TextField()
	alt = TextField()
	text = TextField()
	category = CharField()
	slug = TextField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Post, Users], safe=True)

initialize_db
