from flask import jsonify, request, g, abort, url_for, current_app
from . import api
from app.models import Hd

#Primary key list: get the hd nbuf list
@api.route('/hd/nbufs')
def get_hd_nbufs():
    hds = Hd.query.limit(1000).all()
    return jsonify({'hd': [item.nbuf for item in hds]})
    # return jsonify({'hd': [item.nbuf&mask for item in hds]})

#get the length of hd nbuf list
@api.route('/hd/count')
def get_hd_count():
    count = Hd.query.count()
    # could not return long type, so use str()
    return str(count)
    # return jsonify({'hd': [item.nbuf&mask for item in hds]})

#get a tuple of Hd table
@api.route('/hd/<nbuf>')
def get_hd(nbuf):
    hd = Hd.query.get(nbuf)
    return jsonify({'hd': hd.to_json()})

