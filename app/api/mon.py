from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Mon


@api.route('/<ip_db>/mon/nbufs/<start_time>')
def get_mon_nbufs(ip_db, start_time):
    try:
        mons =getattr(Mon,ip_db).with_entities(Mon.nbuf, Mon.now, Mon.time).filter(Mon.time>start_time).order_by(Mon.now).limit(200).all()
        return jsonify({'mon_nbufs': [item.nbuf for item in mons], 'mon_nows': [item.now for item in mons], 'mon_times': [item.time for item in mons]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
    # return jsonify({'mon': [item.now&mask for item in mons]})

# get the length of mon now list

@api.route('/<ip_db>/mon/<nbuf>')
@cache.cached(timeout=3600)
def get_mon(ip_db, nbuf):

    ## This will print a value into the command prompt with the first nbuf value that works
    # print "---------------- getattr >"
    # print getattr(Mon,ip_db).first().nbuf
    # print "---------------- getattr <"
    try:
        mon =getattr(Mon,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'mon': mon.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
