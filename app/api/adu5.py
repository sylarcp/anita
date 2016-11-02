from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Adu5_pat, Adu5_vtg, Adu5_sat
#from ..sql import and_

@api.route('/<ip_db>/adu5_pat/nbufs/<start_time>')
def get_adu5_pat_nbufs(ip_db, start_time):
    try:
        adu5_pats =getattr(Adu5_pat,ip_db).with_entities(Adu5_pat.nbuf, Adu5_pat.now, Adu5_pat.time).filter(Adu5_pat.time>start_time).order_by(Adu5_pat.now).limit(200).all()
        return jsonify({'adu5_pat_nbufs': [item.nbuf for item in adu5_pats], 'adu5_pat_nows': [item.now for item in adu5_pats], 'adu5_pat_times': [item.time for item in adu5_pats]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_vtg/nbufs/<start_time>')
def get_adu5_vtg_nbufs(ip_db, start_time):
    try:
        adu5_vtgs =getattr(Adu5_vtg,ip_db).with_entities(Adu5_vtg.nbuf, Adu5_vtg.now, Adu5_vtg.time).filter(Adu5_vtg.time>start_time).order_by(Adu5_vtg.now).limit(200).all()
        return jsonify({'adu5_vtg_nbufs': [item.nbuf for item in adu5_vtgs], 'adu5_vtg_nows': [item.now for item in adu5_vtgs], 'adu5_vtg_times': [item.time for item in adu5_vtgs]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_sat/nbufs/<start_time>')
def get_adu5_sat_nbufs(ip_db, start_time):
    try:
        adu5_sats =getattr(Adu5_sat,ip_db).with_entities(Adu5_sat.nbuf, Adu5_sat.now, Adu5_sat.time).filter(Adu5_sat.time>start_time).order_by(Adu5_sat.now).limit(200).all()
        return jsonify({'adu5_sat_nbufs': [item.nbuf for item in adu5_sats], 'adu5_sat_nows': [item.now for item in adu5_sats], 'adu5_sat_times': [item.time for item in adu5_sats]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_pat/<nbuf>')
@cache.cached(timeout=3600)
def get_adu5_pat(ip_db, nbuf):
    try:
        adu5_pat_a =getattr(Adu5_pat,ip_db).filter_by(nbuf=nbuf).filter_by(gpstype=131072).first()
        #adu5_pat_a =getattr(Adu5_pat,ip_db).filter(and_(Adu5_pat.ip_db.nbuf == nbuf, Adu5_pat.ip_db.gpstype=131072)).first()
        # print ''
        # print '****'
        # print getattr(Adu5_pat,ip_db).filter_by(nbuf=nbuf).filter_by(gpstype=131072).first()
        # print ''
        # print ''
        # print '---'
        # print getattr(Adu5_pat,ip_db).filter_by(nbuf=nbuf).filter_by(gpstype=262144).first()
        adu5_pat_b =getattr(Adu5_pat,ip_db).filter_by(nbuf=nbuf).filter_by(gpstype=262144).first()
        #adu5_pat_a =getattr(Adu5_pat,ip_db).filter(and_(Adu5_pat.ip_db.nbuf==nbuf, Adu5_pat.ip_db.gpstype=262144)).first()
        if adu5_pat_a != None:
        	print 'hello adu5_pat_a filled'
        else:
        	print 'HERRORLLO adu5_pat_a not filled'

        if adu5_pat_b != None:
        	print'hello adu5_pat_b filled'
        else:
        	print 'HERRORLLO adu5_pat_b not filled'

        if adu5_pat_b != None and adu5_pat_a != None:
        	print 'SUCESS BOTH BULLSHITS FILLED'
        elif adu5_pat_b == None and adu5_pat_a == None:
        	print 'THAT"S A FUCKIN SHAME; NEITHER ARE FILLED'
        else:
        	print 'FUCK YOU FOR FOUCKING ME YOU FUCKING TWAT! btw only one is (not)filled'

        if adu5_pat_b != None or adu5_pat_a != None:
        	print 'ONE OF THEM IS FILLED'
        elif adu5_pat_b ==None or adu5_pat_b == None:
        	print 'ONE OF THEM IS NOT FILLED'
        else:
        	print 'BOTH ARE FILLED OR NOT FILLED'
        
        if adu5_pat_a == None:
            return jsonify({'pat_b': adu5_pat_b.to_json()})
        elif adu5_pat_b == None:
            return jsonify({'pat_a': adu5_pat_a.to_json()})
        else:
            return jsonify({'pat_a': adu5_pat_a.to_json(), 'pat_b': adu5_pat_b.to_json()}) 

    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_sat/<nbuf>')
@cache.cached(timeout=3600)
def get_adu5_sat(ip_db, nbuf):
    try:
        adu5_sat =getattr(Adu5_sat,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'sat': adu5_sat.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_vtg/<nbuf>')
@cache.cached(timeout=3600)
def get_adu5_vtg(ip_db, nbuf):
    try:
#    print ""
#    print getattr(Adu5_vtg,ip_db).first().nbuf
        adu5_vtg =getattr(Adu5_vtg,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'vtg': adu5_vtg.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

