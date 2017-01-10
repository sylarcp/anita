from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Hk


@api.route('/<ip_db>/hk/nbufs/<offset>')
def get_hk_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Hk,engine_ip_db)
        hks = engine.execute('select nbuf, now, time from hk offset ' + offset + ' limit 20000;').fetchall()
        return jsonify({'hk_nbufs': [item[0] for item in hks], 'hk_nows': [item[1] for item in hks], 'hk_times': [item[2] for item in hks]})
        # hks =getattr(Hk,ip_db).with_entities(Hk.nbuf, Hk.now, Hk.time).filter(Hk.now>offset).order_by(Hk.now, Hk.time).limit(200).all()
        # return jsonify({'hk_nbufs': [item.nbuf for item in hks], 'hk_nows': [item.now for item in hks], 'hk_times': [item.time for item in hks]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# get the length of hk now list


@api.route('/<ip_db>/hk/count')
def get_hk_count(ip_db):
    try:
        count =getattr(Hk,ip_db).count()
        # could not return long type, so use str()
        return str(count)
        # return jsonify({'hk': [item.now&mask for item in hks]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# get a tuple of Hk table


@api.route('/<ip_db>/hk/<nbuf>')
# @cache.cached(timeout=3600)
def get_hk(ip_db, nbuf):
    try:
        hk =getattr(Hk,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'hk': hk.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})