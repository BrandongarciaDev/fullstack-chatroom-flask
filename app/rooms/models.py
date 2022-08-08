# local modules and libraries
from app import db


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
    room_key = db.Column(db.VARCHAR(40), unique=True)
    is_private = db.Column(db.Boolean, nullable=False , default=False)
    category = db.Column(db.INTEGER,
                         db.ForeignKey('category.id', ondelete='cascade',
                                       onupdate='cascade'),
                         nullable=False)
    rooms_pool = db.relationship('RoomsPool', backref='Room')

    def __repr__(self):
        return f'Room: {self.title}'


class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(120), nullable=False)
    description = db.Column(db.TEXT)
    rooms_pool = db.relationship('RoomsPool', backref='Roles')

    def __repr__(self):
        return f'Role: {self.name}'


class RoomsPool(db.Model):
    __tablename__ = 'roomspool'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    room_id = db.Column(db.VARCHAR(100), db.ForeignKey('room.id', ondelete='restrict'), nullable=False)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id', ondelete='restrict'), nullable=False)
    role_id = db.Column(db.INTEGER, db.ForeignKey('roles.id', ondelete='restrict'), nullable=False)

    def __repr__(self):
        return f"""room_id : {self.room_id}
                   user_id : {self.user_id}
                   role_id: {self.role_id}   
        """
