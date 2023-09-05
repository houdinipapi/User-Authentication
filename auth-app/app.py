from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

# Creating an instance for flask_login
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Other Instances
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


# Creating Flask instance within a function --> allows for multiple application instances
def create_app():
    app = Flask(__name__)

    app.secret_key = "724c38e21bcdacee28e0bf3ec0f1abd3"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    return app
