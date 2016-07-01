from flask import jsonify, request, g, abort, url_for, current_app, session
from . import api
from app.models import Slow

#Primary key list:  get the slow time list
@api.route('/<ip_db>/slow/times/<start_time>')
def get_slow_times(ip_db, start_time):
    slows =getattr(Slow,ip_db).with_entities(Slow.nbuf, Slow.now, Slow.time).filter(Slow.time>start_time).order_by(Slow.now).limit(200).all()
    return jsonify({'slow_times': [item.time for item in slows], 'slow_nows': [item.now for item in slows], 'slow_times': [item.time for item in slows]})

#get the length of slow time list
@api.route('/<ip_db>/slow/count')
def get_slow_count(ip_db):
    count = getattr(Slow,ip_db).count()
    # could not return long type, so use str()
    return str(count)

#get a tuple of slow table
@api.route('/<ip_db>/slow/<time>')
def get_slow(ip_db, time):
    slow = getattr(Slow,ip_db).filter_by(time=time).first()
    return jsonify({'slow': slow.to_json()})
