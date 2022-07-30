# third party libraries
from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import login_required

# local modules and libraries
from .models import Room


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
