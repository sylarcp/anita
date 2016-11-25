from flask import jsonify, request, g, abort, url_for, current_app, session
from . import api
from .. import cache
from app.models import Slow

#Primary key list:  get the slow time list
@api.route('/<ip_db>/slow/times/<offset>')
def get_slow_times(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Slow,engine_ip_db)
        slows = engine.execute('select nbuf, now, time from slow offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'slow_nbufs': [item[0] for item in slows], 'slow_nows': [item[1] for item in slows], 'slow_times': [item[2] for item in slows]})
        # slows =getattr(Slow,ip_db).with_entities(Slow.nbuf, Slow.now, Slow.time).filter(Slow.now>offset).order_by(Slow.now).limit(200).all()
        # return jsonify({'slow_times': [item.time for item in slows], 'slow_nows': [item.now for item in slows], 'slow_times': [item.time for item in slows]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
#get the length of slow time list
@api.route('/<ip_db>/slow/count')
# @cache.cached(timeout=3600)
def get_slow_count(ip_db):
    try:
        count = getattr(Slow,ip_db).count()
        # could not return long type, so use str()
        return str(count)
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
#get a tuple of slow table
@api.route('/<ip_db>/slow/<time>')
# @cache.cached(timeout=3600)
def get_slow(ip_db, time):
    try:
        slow = getattr(Slow,ip_db).filter_by(time=time).first()
        return jsonify({'slow': slow.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
