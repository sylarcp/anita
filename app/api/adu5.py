from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Adu5_pat, Adu5_vtg, Adu5_sat

@api.route('/<ip_db>/adu5_pat/nbufs/<offset>')
def get_adu5_pat_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Adu5_pat,engine_ip_db)
        adu5_pats = engine.execute('select nbuf, now, time from adu5_pat offset ' + offset + ' limit 20000;').fetchall()
        return jsonify({'adu5_pat_nbufs': [item[0] for item in adu5_pats], 'adu5_pat_nows': [item[1] for item in adu5_pats], 'adu5_pat_times': [item[2] for item in adu5_pats]})
        # adu5_pats =getattr(Adu5_pat,ip_db).with_entities(Adu5_pat.nbuf, Adu5_pat.now, Adu5_pat.time).filter(Adu5_pat.now>offset).order_by(Adu5_pat.now).limit(200).all()
        # return jsonify({'adu5_pat_nbufs': [item.nbuf for item in adu5_pats], 'adu5_pat_nows': [item.now for item in adu5_pats], 'adu5_pat_times': [item.time for item in adu5_pats]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_vtg/nbufs/<offset>')
def get_adu5_vtg_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Adu5_vtg,engine_ip_db)
        adu5_vtgs = engine.execute('select nbuf, now, time from adu5_vtg offset ' + offset + ' limit 20000;').fetchall()
        return jsonify({'adu5_vtg_nbufs': [item[0] for item in adu5_vtgs], 'adu5_vtg_nows': [item[1] for item in adu5_vtgs], 'adu5_vtg_times': [item[2] for item in adu5_vtgs]})
        # adu5_vtgs =getattr(Adu5_vtg,ip_db).with_entities(Adu5_vtg.nbuf, Adu5_vtg.now, Adu5_vtg.time).filter(Adu5_vtg.now>offset).order_by(Adu5_vtg.now).limit(200).all()
        # return jsonify({'adu5_vtg_nbufs': [item.nbuf for item in adu5_vtgs], 'adu5_vtg_nows': [item.now for item in adu5_vtgs], 'adu5_vtg_times': [item.time for item in adu5_vtgs]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_sat/nbufs/<offset>')
def get_adu5_sat_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Adu5_sat,engine_ip_db)
        adu5_sats = engine.execute('select nbuf, now, time from adu5_sat offset ' + offset + ' limit 20000;').fetchall()
        return jsonify({'adu5_sat_nbufs': [item[0] for item in adu5_sats], 'adu5_sat_nows': [item[1] for item in adu5_sats], 'adu5_sat_times': [item[2] for item in adu5_sats]})
        # adu5_sats =getattr(Adu5_sat,ip_db).with_entities(Adu5_sat.nbuf, Adu5_sat.now, Adu5_sat.time).filter(Adu5_sat.now>offset).order_by(Adu5_sat.now).limit(200).all()
        # return jsonify({'adu5_sat_nbufs': [item.nbuf for item in adu5_sats], 'adu5_sat_nows': [item.now for item in adu5_sats], 'adu5_sat_times': [item.time for item in adu5_sats]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
@api.route('/<ip_db>/adu5_pat/<time>')
def get_adu5_pat_time(ip_db, time):
    try:
        adu5_pat_a =getattr(Adu5_pat,ip_db).filter_by(time=time).filter_by(gpstype=131072).first()
        adu5_pat_b =getattr(Adu5_pat,ip_db).filter_by(time=time).filter_by(gpstype=262144).first()
        if adu5_pat_a == None:
            return jsonify({'pat_b': adu5_pat_b.to_json()})
        elif adu5_pat_b == None:
            return jsonify({'pat_a': adu5_pat_a.to_json()})
        else:
            return jsonify({'pat_a': adu5_pat_a.to_json(), 'pat_b': adu5_pat_b.to_json()}) 
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# @api.route('/<ip_db>/adu5_sat/<nbuf>')
# # @cache.cached(timeout=3600)
# def get_adu5_sat(ip_db, nbuf):
#     try:
#         adu5_sat =getattr(Adu5_sat,ip_db).filter_by(nbuf=nbuf).first()
#         return jsonify({'sat': adu5_sat.to_json()})
#     except BaseException as error:
#         print('Invalid request: {}', format(error))
#         return jsonify({})
@api.route('/<ip_db>/adu5_sat/<time>')
def get_adu5_sat_time(ip_db, time):
    try:
        adu5_sat_a =getattr(Adu5_sat,ip_db).filter_by(time=time).filter_by(gpstype=131072).first()
        adu5_sat_b =getattr(Adu5_sat,ip_db).filter_by(time=time).filter_by(gpstype=262144).first()
        if adu5_sat_a == None:
            return jsonify({'sat_b': adu5_sat_b.to_json()})
        elif adu5_sat_b == None:
            return jsonify({'sat_a': adu5_sat_a.to_json()})
        else:
            return jsonify({'sat_a': adu5_sat_a.to_json(), 'sat_b': adu5_sat_b.to_json()}) 
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

@api.route('/<ip_db>/adu5_vtg/<time>')
def get_adu5_vtg_time(ip_db, time):
    try:
        adu5_vtg_a =getattr(Adu5_vtg,ip_db).filter_by(time=time).filter_by(gpstype=131072).first()
        adu5_vtg_b =getattr(Adu5_vtg,ip_db).filter_by(time=time).filter_by(gpstype=262144).first()
        if adu5_vtg_a == None:
            return jsonify({'vtg_b': adu5_vtg_b.to_json()})
        elif adu5_vtg_b == None:
            return jsonify({'vtg_a': adu5_vtg_a.to_json()})
        else:
            return jsonify({'vtg_a': adu5_vtg_a.to_json(), 'vtg_b': adu5_vtg_b.to_json()}) 
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# @cache.cached(timeout=3600)
# def get_adu5_vtg(ip_db, nbuf):
#     try:
# #    print ""
# #    print getattr(Adu5_vtg,ip_db).first().nbuf
#         adu5_vtg =getattr(Adu5_vtg,ip_db).filter_by(nbuf=nbuf).first()
#         return jsonify({'vtg': adu5_vtg.to_json()})
#     except BaseException as error:
#         print('Invalid request: {}', format(error))
#         return jsonify({})
import datetime
def unix2cesium(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')
@api.route('/<ip_db>/czml')
def get_czml(ip_db):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Adu5_pat,engine_ip_db)
        results = getattr(Adu5_pat,ip_db).with_entities(Adu5_pat.time, Adu5_pat.longitude, Adu5_pat.latitude, Adu5_pat.altitude).filter_by(gpstype=0x20000).filter_by(flag=0).order_by(Adu5_pat.time).all()
        # adu5_pat_b =getattr(Adu5_pat,ip_db).filter_by(time=time).filter_by(gpstype=262144).first()
        starttime = results[0][0]
        endtime = results[-1][0]
        data = []
        for result in results:
            data.append(result[0] - starttime)
            data.append(result[1])
            data.append(result[2])
            data.append(result[3])

        return jsonify({'data': data, 'starttime': starttime, 'endtime': endtime})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
