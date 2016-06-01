from flask import jsonify, request, g, abort, url_for, current_app, session
from . import api
from app.models import Slow

#Primary key list:  get the slow time list
@api.route('/slow/times')
def get_slow_times():
    slows = getattr(Slow,session['ip_db']).limit(1000).all()
    return jsonify({'slow_times': [item.time for item in slows]})

#get the length of slow time list
@api.route('/slow/count')
def get_slow_count():
    count = getattr(Slow,session['ip_db']).count()
    # could not return long type, so use str()
    return str(count)

#get a tuple of slow table
@api.route('/slow/<time>')
def get_slow(time):
    slow = getattr(Slow,session['ip_db']).get(time)
    return jsonify({'slow': slow.to_json()})
