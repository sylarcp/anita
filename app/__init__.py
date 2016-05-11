from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from config import config
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object(config[config_name])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gui:AniTa08@128.175.112.125/anita_0116d'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
from .api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')
