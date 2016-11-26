from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import G12_pos, G12_sat

@api.route('/<ip_db>/g12_pos/nbufs/<offset>')
def get_g12_pos_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(G12_pos,engine_ip_db)
        g12_poss = engine.execute('select nbuf, now, time from g12_pos offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'g12_pos_nbufs': [item[0] for item in g12_poss], 'g12_pos_nows': [item[1] for item in g12_poss], 'g12_pos_times': [item[2] for item in g12_poss]})
        # g12_poss =getattr(G12_pos,ip_db).with_entities(G12_pos.nbuf, G12_pos.now, G12_pos.time).filter(G12_pos.now>offset).order_by(G12_pos.now).limit(200).all()
        # return jsonify({'g12_pos_nbufs': [item.nbuf for item in g12_poss], 'g12_pos_nows': [item.now for item in g12_poss], 'g12_pos_times': [item.time for item in g12_poss]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/g12_sat/nbufs/<offset>')
def get_g12_sat_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(G12_sat,engine_ip_db)
        g12_sats = engine.execute('select nbuf, now, time from g12_sat offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'g12_sat_nbufs': [item[0] for item in g12_sats], 'g12_sat_nows': [item[1] for item in g12_sats], 'g12_sat_times': [item[2] for item in g12_sats]})
        # g12_sats =getattr(G12_sat,ip_db).with_entities(G12_sat.nbuf, G12_sat.now, G12_sat.time).filter(G12_sat.now>offset).order_by(G12_sat.now).limit(200).all()
        # return jsonify({'g12_sat_nbufs': [item.nbuf for item in g12_sats], 'g12_sat_nows': [item.now for item in g12_sats], 'g12_sat_times': [item.time for item in g12_sats]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/g12_pos/<nbuf>')
# @cache.cached(timeout=3600)
def get_g12_pos(ip_db, nbuf):
    try:
        g12_pos =getattr(G12_pos,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'pos': g12_pos.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/g12_sat/<nbuf>')
# @cache.cached(timeout=3600)
def get_g12_sat(ip_db, nbuf):
    try:
#    print ""
#    print getattr(G12_sat,ip_db).first().nbuf
        g12_sat =getattr(G12_sat,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'sat': g12_sat.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

