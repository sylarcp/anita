from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from config import config
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from app.database import init_db
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cache import Cache
# from flask.ext.login import AnonymousUserMixin


app = Flask(__name__)
app.debug = True
app.secret_key = "super secret key"

def create_app():
	#I remove sqlAlchemy object db. Instead we have init_db() give us tables class for use.
	init_db()
	# app = Flask(__name__)

	bootstrap = Bootstrap(app)
	moment = Moment(app)
	login_manager = LoginManager(app)
	toolbar = DebugToolbarExtension(app)
	cache = Cache(app,config={'CACHE_TYPE': 'simple'})

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')
	return app
