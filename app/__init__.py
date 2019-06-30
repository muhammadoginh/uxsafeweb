from flask import Flask
from flask_login import LoginManager
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler

login_manager = LoginManager()


def register_extensions(app):
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('error', 'home', 'landingpage', 'layout', 'login', 'task'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_logs(app):
    basicConfig(filename='error.log', level=DEBUG)
    logger = getLogger()
    logger.addHandler(StreamHandler())


def create_app():
    app = Flask(__name__, static_folder='layout/static')
    register_extensions(app)
    register_blueprints(app)
    configure_logs(app)
    return app