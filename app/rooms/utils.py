from flask_login import current_user, mixins

from ..rooms.models import RoomsPool, Room
from ..auth.models import User


def get_user_rooms():
    print(isinstance(current_user, mixins.AnonymousUserMixin))
    if not isinstance(current_user, mixins.AnonymousUserMixin):
        user_rooms = Room.query.join(RoomsPool, Room.id == RoomsPool.room_id).join(User,
                                                                                   RoomsPool.user_id == User.id).filter(
            User.id == current_user.id).all()

        return user_rooms

    return Room.query.all()
