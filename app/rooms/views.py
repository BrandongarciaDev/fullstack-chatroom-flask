# third party libraries
import json
import os.path

from flask import Blueprint, render_template, abort, session
from flask_login import login_required, current_user
from flask_socketio import emit, join_room
from werkzeug.utils import secure_filename

from app import db, socketio
from .forms import CreateRoom
# local modules and libraries
from .models import Room, Category, RoomsPool
from .utils import generate_room_key
from ..rooms.models import Messages

rooms = Blueprint('rooms', __name__, static_folder='static',
                  template_folder='templates',
                  static_url_path='/chatrooms')
rooms_users = {}


@rooms.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@rooms.route('/chatrooms/<room_id>', methods=['GET', 'POST'])
@login_required
def room(room_id):
    room_data = Room.query.filter_by(id=room_id).first()
    if room_id is None:
        abort(404)
    print("room data is: ", room_data)
    session['data'] = room_data.id

    return render_template('chatroom.html')


@socketio.on('load_messages')
def show_messages():
    room_id_data = session['data']
    room_list_messages = Messages.query.filter_by(from_room=room_id_data, belongs_to=current_user.id).order_by(
        Messages.created_at.asc()).all()

    messages = []
    for message in room_list_messages:
        print(message)
        messages.append({
            'message': message.message,
            'belongs_to': message.belongs_to,
            'created_at': str(message.created_at)
        }
        )

    messages = json.dumps(messages)
    print(messages)

    emit('load_messages', messages, to=room_id_data, broadcast=True)


@socketio.on('disconnect')
def remove_user():
    room_id_data = session['data']
    user = current_user.id
    del rooms_users[room_id_data][user]
    connected = json.dumps(list(rooms_users[room_id_data].values()))
    emit('chatting', connected, to=room_id_data, broadcast=True)


@socketio.on('chatting')
def chatting_room(data):
    room_id_data = session['data']
    # Get all message from specifi room
    rooms_users.setdefault(room_id_data, {})[current_user.id] = {
        'url': '/profile/static/images/' + current_user.profile_image, 'id': current_user.name}
    join_room(room_id_data)
    connected = json.dumps(list(rooms_users[room_id_data].values()))
    emit('chatting', connected, to=room_id_data, broadcast=True)


@rooms.route('/chatrooms/create_room', methods=['GET', 'POST'])
@login_required
def create_room():
    filename = ""
    form = CreateRoom()
    form.category.choices = [(category.id, category.name) for category in Category.query.all()]
    if form.validate_on_submit():
        room_key = generate_room_key()
        image = form.image.data
        filename = secure_filename(image.filename)
        new_filename = room_key + "-" + filename

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
