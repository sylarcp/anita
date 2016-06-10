from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Hk

# Primary key list: get the hk nbuf list

@api.route('/<ip_db>/hk/nbufs')
def get_hk_nbufs(ip_db):
    # print session['ip']
    # print session['db']
    # print session['ip_db']
    hks =getattr(Hk,ip_db).limit(1000).all()
    return jsonify({'hk': [item.nbuf for item in hks]})
    # return jsonify({'hk': [item.nbuf&mask for item in hks]})

# get the length of hk nbuf list


@api.route('/<ip_db>/hk/count')
def get_hk_count(ip_db):
    count =getattr(Hk,ip_db).count()
    # could not return long type, so use str()
    return str(count)
    # return jsonify({'hk': [item.nbuf&mask for item in hks]})

# get a tuple of Hk table


@api.route('/<ip_db>/hk/<nbuf>')
def get_hk(ip_db, nbuf):

    hk =getattr(Hk,ip_db).get(nbuf)
    return jsonify({'hk': hk.to_json()})
