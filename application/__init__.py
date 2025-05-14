from flask import Flask, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import config

db = SQLAlchemy()
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # moduls
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_bp)

    return app

def get_locale(config_name):
    return request.accept_languages.best_match(config[config_name].LOCALES)

def get_timezone(config_name):
    return config[config_name].DEFAULT_TIMEZONE