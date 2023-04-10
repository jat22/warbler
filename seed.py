"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follows, Likes


db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follows, DictReader(follows))

db.session.commit()

like1 = Likes(user_id=3, message_id=25)
like2 = Likes(user_id=3, message_id=67)
like3= Likes(user_id=68, message_id=201)

db.session.add_all([like1, like2, like3])
db.session.commit()