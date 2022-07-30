# Third party libraries
from flask import Blueprint, render_template, request

# local libraries and modules
from ..rooms.models import Category, Room

home = Blueprint('home', __name__, static_folder='static',
                 template_folder='templates',
                 static_url_path='/home/static')


@home.route('/', methods=['GET', 'POST'])
def main_content():
    categories = Category.query.all()
    rooms = Room.query.filter_by(category=1).all()
    if request.method == 'POST':
        rooms = Room.query.filter_by(category=str(*request.form)).all()
    return render_template('home.html', categories=categories, rooms=rooms)

@home.route('/testing')
def testing():
    return render_template('home.html')
