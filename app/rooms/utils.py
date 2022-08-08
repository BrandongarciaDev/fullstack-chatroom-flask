import random
import string

from flask_login import current_user, mixins

from ..auth.models import User
from ..rooms.models import RoomsPool, Room
from .models import Category


def get_user_rooms():
    print(isinstance(current_user, mixins.AnonymousUserMixin))
    if not isinstance(current_user, mixins.AnonymousUserMixin):
        user_rooms = Room.query.join(RoomsPool, Room.id == RoomsPool.room_id).join(User,
                                                                                   RoomsPool.user_id == User.id).filter(
            User.id == current_user.id).all()

        return user_rooms

    return Room.query.all()


def generate_room_key():
    x = None
    found = None
    while found == None:
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        print(x)
        found = Room.query.filter_by(room_key=x)

    return x


