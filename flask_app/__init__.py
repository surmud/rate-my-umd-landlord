# 3rd-party packages
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_login import (
    LoginManager,
)
from flask_talisman import Talisman
from flask_bcrypt import Bcrypt
import os

# stdlib
from datetime import datetime


db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()

from .routes import main
from .users.routes import users
from .landlords.routes import landlords

def page_not_found(e):
    return render_template("404.html"), 404

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["MONGODB_HOST"] = os.getenv("MONGODB_HOST")
    csp = {
        'script-src': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'
    }

    #app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    Talisman(app, content_security_policy=csp)

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(landlords)
    app.register_error_handler(404, page_not_found)

    login_manager.login_view = "users.login"

    return app