from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Hk

# Primary key list: get the hk now list

@api.route('/<ip_db>/hk/nows')
def get_hk_nows(ip_db):
    # print session['ip']
    # print session['db']
    # print session['ip_db']
    hks =getattr(Hk,ip_db).limit(1000).all()
    return jsonify({'hk': [item.now for item in hks]})
    # return jsonify({'hk': [item.now&mask for item in hks]})

# get the length of hk now list


@api.route('/<ip_db>/hk/count')
def get_hk_count(ip_db):
    count =getattr(Hk,ip_db).count()
    # could not return long type, so use str()
    return str(count)
    # return jsonify({'hk': [item.now&mask for item in hks]})

# get a tuple of Hk table


@api.route('/<ip_db>/hk/<now>')
def get_hk(ip_db, now):

    hk =getattr(Hk,ip_db).filter_by(now=now).first()
    return jsonify({'hk': hk.to_json()})
