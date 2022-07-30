from flask import Blueprint
from flask_login import login_required


user_profile = Blueprint('user_profile', __name__,
                         static_folder='static', template_folder='templates',
                         static_url_path='/profile/templates')


@user_profile.route('/profile')
@login_required
def profile():
    return 'you are in profile'
