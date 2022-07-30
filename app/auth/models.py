# absolute modules or libraries
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# local modules and libraries
from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(100), index=True, nullable=False)
    email = db.Column(db.VARCHAR(120), index=True, nullable=False)
    password_hash = db.Column(db.VARCHAR(150), nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Can't show this attribute")

    @password.setter
    def password(self, password):
        print("generating password")
        self.password_hash = generate_password_hash(password)

    def verify_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User: {self.name}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
