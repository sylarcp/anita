from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Hd


# Primary key list: get the hd nbuf list

@api.route('/<ip_db>/hd/nbufs')
def get_hd_nbufs(ip_db):
    print 'connected'
    # print session['ip']
    # print session['db']
    # print session['ip_db']
    hds =getattr(Hd,ip_db).limit(1000).all()
    return jsonify({'hd_nbufs': [item.nbuf for item in hds], 'hd_evnums': [item.evnum for item in hds]})
    # return jsonify({'hd': [item.nbuf&mask for item in hds]})

# get the length of hd nbuf list


@api.route('/<ip_db>/hd/count')
def get_hd_count(ip_db):
    count =getattr(Hd,ip_db).count()
    # could not return long type, so use str()
    return str(count)
    # return jsonify({'hd': [item.nbuf&mask for item in hds]})

# get a tuple of Hd table


@api.route('/<ip_db>/hd/<nbuf>')
def get_hd(ip_db, nbuf):

    hd =getattr(Hd,ip_db).get(nbuf)
    return jsonify({'hd': hd.to_json()})

