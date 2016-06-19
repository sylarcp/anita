from flask import jsonify, request, g, abort, url_for, current_app, session
from . import api
from app.models import Slow

#Primary key list:  get the slow time list
@api.route('/<ip_db>/slow/nows')
def get_slow_nows(ip_db):
    slows = getattr(Slow,ip_db).limit(1000).all()
    return jsonify({'slow_nows': [item.now for item in slows]})

#get the length of slow time list
@api.route('/<ip_db>/slow/count')
def get_slow_count(ip_db):
    count = getattr(Slow,ip_db).count()
    # could not return long type, so use str()
    return str(count)

#get a tuple of slow table
@api.route('/<ip_db>/slow/<now>')
def get_slow(ip_db, now):
    slow = getattr(Slow,ip_db).filter_by(now=now).first()
    return jsonify({'slow': slow.to_json()})
