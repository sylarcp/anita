from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Sshk

# Primary key list: get the sshk now list

@api.route('/<ip_db>/sshk/nbufs/<offset>')
def get_sshk_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Sshk,engine_ip_db)
        sshks = engine.execute('select nbuf, now, time from sshk offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'sshk_nbufs': [item[0] for item in sshks], 'sshk_nows': [item[1] for item in sshks], 'sshk_times': [item[2] for item in sshks]})
        # sshks =getattr(Sshk,ip_db).with_entities(Sshk.nbuf, Sshk.now, Sshk.time).filter(Sshk.now>offset).order_by(Sshk.now).limit(200).all()
        # return jsonify({'sshk_nbufs': [item.nbuf for item in sshks], 'sshk_nows': [item.now for item in sshks], 'sshk_times': [item.time for item in sshks]})
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
# @cache.cached(timeout=3600)
def get_sshk(ip_db, nbuf):
    try:
        print 'hello'
        sshk =getattr(Sshk,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'sshk': sshk.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})