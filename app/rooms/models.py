# local modules and libraries
from app import db
from flask_login import UserMixin


# models
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(50), nullable=False)
    description = db.Column(db.TEXT)
    room = db.relationship('Room', backref='Category', lazy=True)

    def __repr__(self):
        return f'Category: {self.name}'


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.VARCHAR(100), primary_key=True, nullable=False)
    title = db.Column(db.VARCHAR(80), index=True, nullable=False)
    description = db.Column(db.TEXT)
    image_url = db.Column(db.TEXT)
    likes = db.Column(db.INTEGER)
    category = db.Column(db.INTEGER,
                         db.ForeignKey('category.id', ondelete='cascade',
                                       onupdate='cascade'),
                         nullable=False)

    def __repr__(self):
        return f'Room: {self.title}'

