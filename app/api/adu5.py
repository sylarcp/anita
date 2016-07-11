from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Adu5_pat, Adu5_vtg, Adu5_sat

@api.route('/<ip_db>/adu5_pat/nbufs/<start_time>')
def get_adu5_pat_nbufs(ip_db, start_time):
    adu5_pats =getattr(Adu5_pat,ip_db).with_entities(Adu5_pat.nbuf, Adu5_pat.now, Adu5_pat.time).filter(Adu5_pat.time>start_time).order_by(Adu5_pat.now).limit(200).all()
    return jsonify({'adu5_pat_nbufs': [item.nbuf for item in adu5_pats], 'adu5_pat_nows': [item.now for item in adu5_pats], 'adu5_pat_times': [item.time for item in adu5_pats]})

@api.route('/<ip_db>/adu5_vtg/nbufs/<start_time>')
def get_adu5_vtg_nbufs(ip_db, start_time):
    adu5_vtgs =getattr(Adu5_vtg,ip_db).with_entities(Adu5_vtg.nbuf, Adu5_vtg.now, Adu5_vtg.time).filter(Adu5_vtg.time>start_time).order_by(Adu5_vtg.now).limit(200).all()
    return jsonify({'adu5_vtg_nbufs': [item.nbuf for item in adu5_vtgs], 'adu5_vtg_nows': [item.now for item in adu5_vtgs], 'adu5_vtg_times': [item.time for item in adu5_vtgs]})

@api.route('/<ip_db>/adu5_sat/nbufs/<start_time>')
def get_adu5_sat_nbufs(ip_db, start_time):
    adu5_sats =getattr(Adu5_sat,ip_db).with_entities(Adu5_sat.nbuf, Adu5_sat.now, Adu5_sat.time).filter(Adu5_sat.time>start_time).order_by(Adu5_sat.now).limit(200).all()
    return jsonify({'adu5_sat_nbufs': [item.nbuf for item in adu5_sats], 'adu5_sat_nows': [item.now for item in adu5_sats], 'adu5_sat_times': [item.time for item in adu5_sats]})

@api.route('/<ip_db>/adu5_pat/<nbuf>')
@cache.cached(timeout=3600)
def get_adu5_pat(ip_db, nbuf):
    adu5_pat =getattr(Adu5_pat,ip_db).filter_by(nbuf=nbuf).first()
    return jsonify({'pat': adu5_pat.to_json()})

@api.route('/<ip_db>/adu5_sat/<nbuf>')
@cache.cached(timeout=3600)
def get_adu5_sat(ip_db, nbuf):
    adu5_sat =getattr(Adu5_sat,ip_db).filter_by(nbuf=nbuf).first()
    return jsonify({'sat': adu5_sat.to_json()})

@api.route('/<ip_db>/adu5_vtg/<nbuf>')
@cache.cached(timeout=3600)
def get_adu5_vtg(ip_db, nbuf):
#    print ""
#    print getattr(Adu5_vtg,ip_db).first().nbuf
    adu5_vtg =getattr(Adu5_vtg,ip_db).filter_by(nbuf=nbuf).first()
    return jsonify({'vtg': adu5_vtg.to_json()})


