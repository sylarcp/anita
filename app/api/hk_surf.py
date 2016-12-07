from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Hk_surf

# Primary key list: get the hk_surf now list

@api.route('/<ip_db>/hk_surf/nbufs/<offset>')
def get_hk_surf_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Hk_surf,engine_ip_db)
        hk_surfs = engine.execute('select nbuf, now, time from hk_surf offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'hk_surf_nbufs': [item[0] for item in hk_surfs], 'hk_surf_nows': [item[1] for item in hk_surfs], 'hk_surf_times': [item[2] for item in hk_surfs]})
        # hk_surfs =getattr(Hk_surf,ip_db).with_entities(Hk_surf.nbuf, Hk_surf.now, Hk_surf.time).filter(Hk_surf.now>offset).order_by(Hk_surf.now).limit(200).all()
        # return jsonify({'hk_surf_nbufs': [item.nbuf for item in hk_surfs], 'hk_surf_nows': [item.now for item in hk_surfs], 'hk_surf_times': [item.time for item in hk_surfs]})
    except BaseException as error:
        print("Invalid request: {'hk_urf_nbufs':[], 'hk_urf_nows': [],  'hk_urf_times': []}",format(error))
        return jsonify({})
# # get the length of hk_surf now list


# @api.route('/<ip_db>/hk_surf/count')
# def get_hk_surf_count(ip_db):
#     try:
#         count =getattr(Hk_surf,ip_db).count()
#         # could not return long type, so use str()
#         return str(count)
#         # return jsonify({'hk_surf': [item.now&mask for item in hk_surfs]})
#     except BaseException as error:
#         print('Invalid request: {}',format(error))
#         return jsonify({})
# get a tuple of Hk_surf table


@api.route('/<ip_db>/hk_surf/<nbuf>')
def get_hk_surf(ip_db, nbuf):
    try:
        hk_surf =getattr(Hk_surf,ip_db).filter_by(nbuf=nbuf).first()
        print 'hk_surf: ' , hk_surf.to_json()
        return jsonify({'hk_surf': hk_surf.to_json()})
    except BaseException as error:
        print('Invalid request: {"hk_surf": {}.to_json()}',format(error))
        return jsonify({})