# Third party libraries
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required
# Local modules and libraries
from .forms import Register, Login
from .models import User
from app import db

auth = Blueprint('auth', __name__, static_folder='static',
                 template_folder='templates',
                 static_url_path='/auth/static')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    print(form.errors)
    if form.validate_on_submit():
        user = User(name=form.username.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully register')

        return redirect(url_for("auth.login"))


    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password_hash(password=form.password.data):
            flash('you are logged in')
            login_user(user)
            return redirect(url_for("user_profile.profile"))

        flash("Please verify the password an email")
    return render_template('login.html', form=form)


