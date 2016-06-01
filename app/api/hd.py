from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Hd


# Primary key list: get the hd nbuf list

@api.route('/hd/nbufs')
def get_hd_nbufs():
    # print session['ip']
    # print session['db']
    # print session['ip_db']
    hds =getattr(Hd,session['ip_db']).limit(1000).all()
    return jsonify({'hd': [item.nbuf for item in hds]})
    # return jsonify({'hd': [item.nbuf&mask for item in hds]})

# get the length of hd nbuf list


@api.route('/hd/count')
def get_hd_count():
    count =getattr(Hd,session['ip_db']).count()
    # could not return long type, so use str()
    return str(count)
    # return jsonify({'hd': [item.nbuf&mask for item in hds]})

# get a tuple of Hd table


@api.route('/hd/<nbuf>')
def get_hd(nbuf):
    print '!!!!!!!!!!!!!!!!!!!!!!!!!'
    print session['ip']
    print session['db']
    hd =getattr(Hd,session['ip_db']).get(nbuf)
    return jsonify({'hd': hd.to_json()})

