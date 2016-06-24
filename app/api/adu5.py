from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Adu5_pat, Adu5_vtg, Adu5_sat

@api.route('/<ip_db>/adu5_pat/nbufs')
def get_adu5_pat_nbufs(ip_db):
    adu5_pats =getattr(Adu5_pat,ip_db).limit(1000).all()
    return jsonify({'adu5_pat_nbufs': [item.nbuf for item in adu5_pats], 'adu5_pat_nows': [item.now for item in adu5_pats]})

@api.route('/<ip_db>/adu5_vtg/nbufs')
def get_adu5_vtg_nbufs(ip_db):
    adu5_vtgs =getattr(Adu5_vtg,ip_db).limit(1000).all()
    return jsonify({'adu5_vtg_nbufs': [item.nbuf for item in adu5_vtgs], 'adu5_vtg_nows': [item.now for item in adu5_vtgs]})

@api.route('/<ip_db>/adu5_sat/nbufs')
def get_adu5_sat_nbufs(ip_db):
    adu5_sats =getattr(Adu5_sat,ip_db).limit(1000).all()
    return jsonify({'adu5_sat_nbufs': [item.nbuf for item in adu5_sats], 'adu5_sat_nows': [item.now for item in adu5_sats]})



@api.route('/<ip_db>/adu5_pat/<nbuf>')
def get_adu5_pat(ip_db, nbuf):
    adu5_pat =getattr(Adu5_pat,ip_db).filter_by(nbuf=nbuf).first()
    return jsonify({'pat': adu5_pat.to_json()})

@api.route('/<ip_db>/adu5_sat/<nbuf>')
def get_adu5_sat(ip_db, nbuf):
    adu5_sat =getattr(Adu5_sat,ip_db).filter_by(nbuf=nbuf).first()
    return jsonify({'sat': adu5_sat.to_json()})

@api.route('/<ip_db>/adu5_vtg/<nbuf>')
def get_adu5_vtg(ip_db, nbuf):
#    print ""
#    print getattr(Adu5_vtg,ip_db).first().nbuf
    adu5_vtg =getattr(Adu5_vtg,ip_db).filter_by(nbuf=nbuf).first()
    return jsonify({'vtg': adu5_vtg.to_json()})


