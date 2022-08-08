# third party libraries
import os.path

from flask import Blueprint, render_template, abort, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .forms import CreateRoom
# local modules and libraries
from .models import Room, Category, RoomsPool
from .utils import generate_room_key
from app import db

rooms = Blueprint('rooms', __name__, static_folder='static',
                  template_folder='templates',
                  static_url_path='/chatrooms')


@rooms.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@rooms.route('/chatrooms/<room_id>')
@login_required
def room(room_id):
    room_data = Room.query.filter_by(id=room_id).first()

    if room_data is None:
        abort(404)
    return 'hi there'


@rooms.route('/chatrooms/create_room', methods=['GET', 'POST'])
@login_required
def create_room():
    filename = ""
    form = CreateRoom()
    form.category.choices = [(category.id, category.name) for category in Category.query.all()]
    if form.validate_on_submit():
        print(form.category.data)
        room_key = generate_room_key()
        image = form.image.data
        filename = secure_filename(image.filename)
        new_filename = room_key + "-" + filename
        print(new_filename)
        image.save(os.path.join(
            rooms.static_folder, 'images', new_filename
        ))

        room = Room(id=form.title.data,
                    title=form.title.data,
                    description=form.description.data,
                    image_url=new_filename,
                    room_key=room_key,
                    category=form.category.data,
                    is_private=True if form.rooms_types.data == 'private' else False
                    )
        rooms_pool = RoomsPool(room_id=form.title.data,
                               user_id=current_user.id,
                               role_id=1)

        db.session.add_all([room, rooms_pool])
        db.session.commit()
        print("you have created a new chatroom")

    return render_template('create_chatroom.html', form=form)
