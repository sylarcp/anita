from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import Base
import psycopg2
import psycopg2.extensions
import select

from app.models import Hd, Wv, Slow, Hk, Sshk, Hk_surf, Turf, Mon, Adu5_pat, Adu5_vtg, Adu5_sat,\
G12_pos, G12_sat, Cmd, Wakeup, File



@api.route('/connect/<ip>/<db>')
def connect(ip,db):
    try:
        port = ''
        # UD's postgres changed port to 54320
        if ip in ['128.175.112.58', '128.175.112.80', '128_175_112_58', '128_175_112_80']:
            port = ':54320'
        engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') + port + '/' + db, convert_unicode=True)
        conn=engine.connect()
        print 'connnected'
        # db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
        db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=conn))
        query_ip_db= 'query_' + ip  + '_' + db
        session_ip_db= 'session_' + ip  + '_' + db
        #  query_ip_db is a string and should be Base's attribute. setattr() is perfect for this job
        setattr(Base,query_ip_db, db_session.query_property())
        # set attribure session_ip_db which is the enigne bind to this object. Use it directly to query for the database would be faster.
        setattr(Base,session_ip_db, db_session.get_bind())
        # flash("Database connect Successful", 'success') # flash message not working, why?
        # hd = getattr(Hd,query_ip_db).with_entities(Hd.nbuf, Hd.evnum, Hd.time, Hd.now).filter(Hd.now>0).order_by(Hd.now, Hd.time).limit(100).all()
        # print [item[0] for item in engine.execute('select nbuf from hd limit 1000;')]
        # print ({'hd_now': [item.now for item in hd]})
        # wv = getattr(Wv,query_ip_db).first()
        # print ({'wv': wv.to_json()})
        
        # hk = getattr(Hk,query_ip_db).first()
        # print ({'hk': hk.to_json()})
        # hds = engine.execute('select nbuf, evnum, time, now from rf offset ' + '10' + ' limit 30;').fetchall()
        # hks = engine.execute('select nbuf, time, now from hk;').fetchall()
        # print 'data is :' + str(len(hks))
        # print [(item[0], item[1], item[2]) for item in hks]

        print 'success'
        return 'success'
    except Exception as error:
        print error
        return 'fail'
@api.route('/getDBnames/<ip>')
def getDBnames(ip):
    port = ''
    # UD's postgres changed port to 54320
    if ip in ['128.175.112.58', '128.175.112.80', '128_175_112_58', '128_175_112_80']:
        port = ':54320'
    engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') + port + '/template1', convert_unicode=True)
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
        elif row["datname"] == 'anita16':
            dbnames_prev.append(row["datname"])
    dbnames = dbnames_prev + dbnames
    return jsonify({'dbnames':dbnames})
