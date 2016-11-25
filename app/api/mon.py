from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Mon


@api.route('/<ip_db>/mon/nbufs/<offset>')
def get_mon_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Mon,engine_ip_db)
        mons = engine.execute('select nbuf, now, time from mon offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'mon_nbufs': [item[0] for item in mons], 'mon_nows': [item[1] for item in mons], 'mon_times': [item[2] for item in mons]})
        # mons =getattr(Mon,ip_db).with_entities(Mon.nbuf, Mon.now, Mon.time).filter(Mon.now>offset).order_by(Mon.now).limit(200).all()
        # return jsonify({'mon_nbufs': [item.nbuf for item in mons], 'mon_nows': [item.now for item in mons], 'mon_times': [item.time for item in mons]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
    # return jsonify({'mon': [item.now&mask for item in mons]})

# get the length of mon now list

@api.route('/<ip_db>/mon/<nbuf>')
# @cache.cached(timeout=3600)
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
