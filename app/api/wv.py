from flask import jsonify, request, g, abort, url_for, current_app, session, Response
from . import api, cache
from app.models import Wv


#Primary key list: get the (evnum, id)
@api.route('/<ip_db>/wv/evnum_ids')
def get_wv_evnum_ids(ip_db):
    wvs =getattr(Wv,ip_db).limit(1000).all()
    return jsonify({'wv': [(item.evnum, item.id) for item in wvs]})

#get the length of wv list
@api.route('/<ip_db>/wv/count')
def get_wv_count(ip_db):
    #Todo how to make it count fask?
    count =getattr(Wv,ip_db).count()
    # could not return long type, so use str()
    return str(count)

#get wv table content for evnum and id
@api.route('/<ip_db>/wv/<int:evnum>/<int:id>')
def get_wv(ip_db, evnum, id):
    wv =getattr(Wv,ip_db).filter_by(evnum=evnum, id=id).first()
    return jsonify({'wv': wv.to_json()})

#get 40 waveforms for a evnum
@api.route('/<ip_db>/wv/<int:evnum>')
@cache.cached(timeout=50)
def get_wvs(ip_db, evnum):
    json_comment={}
    wvs =getattr(Wv,ip_db).filter_by(evnum=evnum).order_by(Wv.id).all()
    for wv in wvs:
        json_comment[wv.id]=wv.to_json()
    return jsonify(json_comment)


