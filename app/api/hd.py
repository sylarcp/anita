from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Hd
from .. import cache


# Primary key list: get the hd nbuf list
@api.route('/<ip_db>/hd/nbufs/<offset>')
def get_hd_nbufs(ip_db, offset):
    try:
        # hds =getattr(Hd,ip_db).with_entities(Hd.nbuf, Hd.evnum, Hd.time, Hd.now).filter(Hd.now>offset).order_by(Hd.now, Hd.time).limit(100).all()
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Hd,engine_ip_db)
        hds = engine.execute('select nbuf, evnum, time, now from rf offset ' + offset + ' limit 30;').fetchall()
        return jsonify({'hd_nbufs': [item[0] for item in hds], 'hd_evnums': [item[1] for item in hds], 'hd_times': [item[2] for item in hds], 'hd_nows': [item[2] for item in hds]})
    except BaseException as error:
        print('Invalid request: get_hd_nbufs()', format(error))
        return jsonify({})

# Primary key list: get the rf nbuf list
@api.route('/<ip_db>/rf/nbufs/<offset>')
def get_rf_nbufs(ip_db, offset):
    try:
        rfs =getattr(Rf,ip_db).with_entities(Rf.nbuf, Rf.evnum, Rf.time, Rf.now).filter(Rf.now>offset).order_by(Rf.now, Rf.time).limit(100).all()
        return jsonify({'rf_nbufs': [item.nbuf for item in rfs], 'rf_evnums': [item.evnum for item in rfs], 'rf_times': [item.time for item in rfs], 'rf_nows': [item.now for item in rfs]})
    except BaseException as error:
        print('Invalid request: get_rf_nbufs()', format(error))
        return jsonify({})

# get the length of hd nbuf list
@api.route('/<ip_db>/hd/count')
def get_hd_count(ip_db):
    try:
        count =getattr(Hd,ip_db).count()
        # could not return long type, so use str()
        return str(count)
        # return jsonify({'hd': [item.nbuf&mask for item in hds]})
    except BaseException as error:
        print('Invalid request: get_hd_count()', format(error))
        return jsonify({})

# get a tuple of Hd table
@api.route('/<ip_db>/hd/<nbuf>')
# @cache.cached(timeout=3600)
def get_hd(ip_db, nbuf):
    print 'api hd'
    try:
        hd =getattr(Hd,ip_db).get(nbuf)
        return jsonify({'hd': hd.to_json()})
    except BaseException as error:
        print('Invalid request: get_hd()', format(error))
        return jsonify({})

