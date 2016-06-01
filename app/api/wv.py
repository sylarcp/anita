from flask import jsonify, request, g, abort, url_for, current_app, session
from . import api
from app.models import Wv
#Primary key list: get the (evnum, id)
# @api.route('/wv/evnum_ids)') 
# @api.route('/wv)') 
# def get_wv_evnum_ids():
#     return '!!!!!!!!!'
#     wvs = Wv.query.limit(1000).all()
#     return jsonify({'wv': [(item.evnum, item.id) for item in wvs]})
@api.route('/wv/evnum_ids')
def get_wv_evnum_ids():
    wvs =getattr(Wv,session['ip_db']).limit(1000).all()
    return jsonify({'wv': [(item.evnum, item.id) for item in wvs]})

#get the length of wv list
@api.route('/wv/count')
def get_wv_count():
    #Todo how to make it count fask?
    count =getattr(Wv,session['ip_db']).count()
    # could not return long type, so use str()
    return str(count)

#get wv table content for evnum and id
@api.route('/wv/<int:evnum>/<int:id>')
def get_wv(evnum, id):
    wv =getattr(Wv,session['ip_db']).filter_by(evnum=evnum, id=id).first()
    return jsonify({'wv': wv.to_json()})

#get 40 waveforms for a evnum
@api.route('/wv/<int:evnum>')
def get_wvs(evnum):
    json_comment={}
    wvs =getattr(Wv,session['ip_db']).filter_by(evnum=evnum).order_by(Wv.id).all()
    for wv in wvs:
        json_comment[wv.id]=wv.to_json()
    return jsonify(json_comment)

