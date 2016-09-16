from flask import jsonify, request, g, abort, url_for, current_app, session, Response
from . import api
from .. import cache
from app.models import Wv


#Primary key list: get the (evnum, id)
@api.route('/<ip_db>/wv/evnum_ids')
def get_wv_evnum_ids(ip_db):
    try:
        wvs =getattr(Wv,ip_db).limit(1000).all()
        return jsonify({'wv': [(item.evnum, item.id) for item in wvs]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

#get the length of wv list
@api.route('/<ip_db>/wv/count') 
def get_wv_count(ip_db):
    try:
        #Todo how to make it count fast?
        count =getattr(Wv,ip_db).count()
        # could not return long type, so use str()
        return str(count)
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

#get wv table content for evnum and id
@api.route('/<ip_db>/wv/<int:evnum>/<int:id>')
# @cache.cached(timeout=3600)
def get_wv(ip_db, evnum, id):
    try:
        wv =getattr(Wv,ip_db).filter_by(evnum=evnum, id=id).first()
        return jsonify({'wv': wv.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

#get 40 waveforms for a evnum
@api.route('/<ip_db>/wv/<int:evnum>')
@cache.cached(timeout=3600)
def get_wvs(ip_db, evnum):
    try:
        json_comment={}
        wvs =getattr(Wv,ip_db).filter_by(evnum=evnum).order_by(Wv.id).all()
        for wv in wvs:
            json_comment[wv.id]=wv.to_json()
            # json_comment[wv.id + 100]=wv.to_json()
        return jsonify(json_comment)
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        return jsonify({})
