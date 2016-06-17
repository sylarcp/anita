from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import Base
import psycopg2
import psycopg2.extensions
import select



@api.route('/connect/<ip>/<db>')
def connect(ip,db):
    engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') +'/' + db, convert_unicode=True)
    conn=engine.connect()
    # db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
    db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=conn))
    query_ip_db= 'query_' + ip  + '_' + db
    #  query_ip_db is a string and should be Base's attribute. setattr() is perfect for this job
    setattr(Base,query_ip_db, db_session.query_property())


    # conn.execute(text("LISTEN rf; LISTEN hd;").execution_options(autocommit=True))
    # print "Waiting for notifications on channels 'rf', 'hd' with SQL Alchemy"
    # while 1:
    #     #conn.commit()
    #     if select.select([conn.connection],[],[],5) == ([],[],[]):
    #         print "Timeout"
    #     else:
    #         conn.connection.poll()
    #         while conn.connection.notifies:
    #             notify = conn.connection.notifies.pop()
    #             print "Got NOTIFY:", datetime.datetime.now(), notify.pid, notify.channel, notify.payload
    return 'success'
