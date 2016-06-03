from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import Base


@api.route('/connect/<ip>/<db>')
def connect(ip,db):
    engine = create_engine('postgresql://gui:AniTa08@128.175.112.58/anita_0107d', convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
    Base.query_128_175_112_58_anita_0107d = db_session.query_property()
    return 'done'

# def init_db():
# 	import app.models
