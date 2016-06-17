from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Mon


@api.route('/<ip_db>/mon/nows')
def get_mon_nows(ip_db):
    # print session['ip']
    # print session['db']
    # print session['ip_db']
    mons =getattr(Mon,ip_db).limit(1000).all()
    return jsonify({'mon': [item.now for item in mons]})
    # return jsonify({'hk': [item.now&mask for item in hks]})

@api.route('/<ip_db>/mon/<now>')
def get_mon(ip_db, now):

	## This will print a value into the command prompt with the first now value that works
	# print "---------------- getattr >"
	# print getattr(Mon,ip_db).first().now
	# print "---------------- getattr <"

	mon =getattr(Mon,ip_db).filter_by(now=now).first()
	return jsonify({'mon': mon.to_json()})

