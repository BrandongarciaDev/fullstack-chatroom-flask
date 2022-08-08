# Third party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# local modules and libraries
from configs import config

# globals
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.register'
    login_manager.login_message = "You must be logged in to access this page."
    migrate = Migrate(app, db)

    from app.rooms import models
    from app.auth import models

    from .home.views import home as home_blueprint
    from .rooms.views import rooms as rooms_blueprint
    from .auth.views import auth as auth_blueprint
    from .profile.views import user_profile as user_profile_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(rooms_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_profile_blueprint)

    return app
