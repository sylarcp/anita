from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from config import config
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from app.database import init_db


def create_app():
	init_db()
	app = Flask(__name__)

	bootstrap = Bootstrap(app)
	moment = Moment(app)
	login_manager = LoginManager(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')
	return app
