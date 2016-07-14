from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Hd
from .. import cache


# Primary key list: get the hd nbuf list

@api.route('/<ip_db>/hd/nbufs/<start_time>')
def get_hd_nbufs(ip_db, start_time):
    try:
        print 'connected', start_time
        hds =getattr(Hd,ip_db).with_entities(Hd.nbuf, Hd.evnum, Hd.time).filter(Hd.time>start_time).order_by(Hd.now).limit(200).all()
        # print str(getattr(Hd,ip_db).with_entities(Hd.nbuf, Hd.evnum).filter(Hd.time>0).order_by(Hd.now).limit(1000))
        return jsonify({'hd_nbufs': [item.nbuf for item in hds], 'hd_evnums': [item.evnum for item in hds], 'hd_times': [item.time for item in hds]})
    except BaseException as error:
        print('Invalid request: get_hd_nbufs()', format(error))
        return jsonify({})
        # return jsonify({'hd': [item.nbuf&mask for item in hds]})

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
@cache.cached(timeout=3600)
def get_hd(ip_db, nbuf):
    try:
        hd =getattr(Hd,ip_db).get(nbuf)
        return jsonify({'hd': hd.to_json()})
    except BaseException as error:
        print('Invalid request: get_hd()', format(error))
        return jsonify({})

