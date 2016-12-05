from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Turf

# Primary key list: get the turf now list

@api.route('/<ip_db>/turf/nbufs/<offset>')
def get_turf_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Turf,engine_ip_db)
        turfs = engine.execute('select nbuf, now, time from turf offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'turf_nbufs': [item[0] for item in turfs], 'turf_nows': [item[1] for item in turfs], 'turf_times': [item[2] for item in turfs]})
        # turfs =getattr(Turf,ip_db).with_entities(Turf.nbuf, Turf.now, Turf.time).filter(Turf.now>offset).order_by(Turf.now).limit(200).all()
        # return jsonify({'turf_nbufs': [item.nbuf for item in turfs], 'turf_nows': [item.now for item in turfs], 'turf_times': [item.time for item in turfs]})
    except BaseException as error:
        print("Invalid request: {'turf_nbufs':[], 'turf_nows': [],  'turf_times': []}",format(error))
        return jsonify({})
# get the length of turf now list


@api.route('/<ip_db>/turf/count')
def get_turf_count(ip_db):
    try:
        count =getattr(Turf,ip_db).count()
        # could not return long type, so use str()
        return str(count)
        # return jsonify({'turf': [item.now&mask for item in turfs]})
    except BaseException as error:
        print('Invalid request: {}',format(error))
        return jsonify({})
# get a tuple of Turf table


@api.route('/<ip_db>/turf/<nbuf>')
# @cache.cached(timeout=3600)
def get_turf(ip_db, nbuf):
    try:
        turf =getattr(Turf,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'turf': turf.to_json()})
    except BaseException as error:
        print('Invalid request: {}',format(error))
        return jsonify({})