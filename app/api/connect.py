from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import Base


@api.route('/connect/<ip>/<db>')
def connect(ip,db):
    engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') +'/' + db, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
    query_ip_db= 'query_' + ip  + '_' + db
    #  query_ip_db is a string and should be Base's attribute. setattr() is perfect for this job
    setattr(Base,query_ip_db, db_session.query_property())
    # if query_ip_db == 'query_128_175_112_125_anita_0116d':
    #     Base.query_128_175_112_125_anita_0116d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_58_anita_0105d':
    #     Base.query_128_175_112_58_anita_0105d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_58_anita_0106d':
    #     Base.query_128_175_112_58_anita_0106d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_58_anita_0107d':
    #     Base.query_128_175_112_58_anita_0107d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_58_anita_0108d':
    #     Base.query_128_175_112_58_anita_0108d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_80_anita_0105d':
    #     Base.query_128_175_112_80_anita_0105d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_80_anita_0106d':
    #     Base.query_128_175_112_80_anita_0106d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_80_anita_0107d':
    #     Base.query_128_175_112_80_anita_0107d= db_session.query_property()
    # elif query_ip_db == 'query_128_175_112_80_anita_0108d':
    #     Base.query_128_175_112_80_anita_0108d= db_session.query_property()
    return 'success'

# def init_db():
# 	import app.models
