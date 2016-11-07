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
    try:
        engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') +'/' + db, convert_unicode=True)
        print 'before conn'
        conn=engine.connect()
        print 'conn'
        # db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
        db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=conn))
        query_ip_db= 'query_' + ip  + '_' + db
        #  query_ip_db is a string and should be Base's attribute. setattr() is perfect for this job
        setattr(Base,query_ip_db, db_session.query_property())
        print '------', getattr(Base,query_ip_db)
        # flash("Database connect Successful", 'success') # flash message not working, why?
        return 'success'
    except Exception as error:
        print error
        return 'fail'
@api.route('/getDBnames/<ip>')
def getDBnames(ip):
    engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') + '/template1', convert_unicode=True)
    conn = engine.connect()
    # rows = conn.execute("SELECT pg_database.datname, pg_database_size(pg_database.datname), pg_size_pretty(pg_database_size(pg_database.datname)) FROM pg_database ORDER BY pg_database_size DESC;")
    rows = conn.execute("SELECT pg_database.datname FROM pg_database order by datname;")
    dbnames_prev = []
    dbnames = []
    for row in rows:
        if row["datname"][:7] == 'anita_1':
            dbnames_prev.append(row["datname"])
        elif row["datname"][:8] == 'anita_01':
            dbnames.append(row["datname"])
    dbnames = dbnames_prev + dbnames
    return jsonify({'dbnames':dbnames})
