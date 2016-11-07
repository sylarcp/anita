from flask import jsonify, request, g, abort, url_for, current_app, session, flash
from flask.ext.login import LoginManager, current_user
from . import api

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import Base
import psycopg2
import psycopg2.extensions
import select

import multiprocessing.pool
import functools

def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator

@timeout(10)
def __connect(engine):
    return engine.connect()

@api.route('/connect/<ip>/<db>')
def connect(ip,db):
    try:
        engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') +'/' + db, convert_unicode=True)
        print 'before conn'
        conn=__connect(engine)
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

