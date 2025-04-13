from flask import Flask
from flask_smorest import Api

from store import commands, order, product, user
from store.error_handler import store_error_handler
from store.extensions import (
    bcrypt,
    db,
    debug_toolbar,
    jwt,
    migrate,
)


def create_app(config_obj="store.settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_obj)
    register_extensions(app)
    register_commands(app)
    register_blueprints(app)
    register_error_handler(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


def register_commands(app):
    app.cli.add_command(commands.create_admin_user)


def register_blueprints(app):
    # Register API Blueprint
    api = Api(app)
    api.register_blueprint(user.apis.blueprint)
    api.register_blueprint(product.apis.blueprint)
    api.register_blueprint(order.apis.blueprint)


def register_error_handler(app):
    store_error_handler(app)
