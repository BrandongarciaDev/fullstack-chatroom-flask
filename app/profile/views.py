# third party libraries
from flask import Blueprint, render_template

from flask_login import login_required
# local imports
from ..rooms import utils

user_profile = Blueprint('user_profile', __name__,
                         static_folder='static', template_folder='templates',
                         static_url_path='/profile/static')


@user_profile.route('/profile')
@login_required
def profile():
    created_rooms = utils.get_user_rooms()
    return render_template("profile.html", rooms=created_rooms, user_rooms=created_rooms)
