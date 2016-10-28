from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Sshk

# Primary key list: get the sshk now list

@api.route('/<ip_db>/sshk/nbufs/<start_time>')
def get_sshk_nbufs(ip_db, start_time):
    try:
        sshks =getattr(Sshk,ip_db).with_entities(Sshk.nbuf, Sshk.now, Sshk.time).filter(Sshk.time>start_time).order_by(Sshk.now).all()
        return jsonify({'sshk_nbufs': [item.nbuf for item in sshks], 'sshk_nows': [item.now for item in sshks], 'sshk_times': [item.time for item in sshks]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# get the length of sshk now list


@api.route('/<ip_db>/sshk/count')
def get_sshk_count(ip_db):
    try:
        count =getattr(Sshk,ip_db).count()
        # could not return long type, so use str()
        return str(count)
        # return jsonify({'sshk': [item.now&mask for item in hks]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# get a tuple of Sshk table


@api.route('/<ip_db>/sshk/<nbuf>')
@cache.cached(timeout=3600)
def get_sshk(ip_db, nbuf):
    try:
        print 'hello'
        sshk =getattr(Sshk,ip_db).filter_by(nbuf=nbuf).first()
        print sshk.to_json()
        return jsonify({'sshk': sshk.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})