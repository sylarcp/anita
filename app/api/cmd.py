from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Cmd


@api.route('/<ip_db>/cmd/nbufs/<offset>')
def get_cmd_nbufs(ip_db, offset):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Cmd,engine_ip_db)
        cmds = engine.execute('select nbuf, now, time from cmd offset ' + offset + ' limit 2000;').fetchall()
        return jsonify({'cmd_nbufs': [item[0] for item in cmds], 'cmd_nows': [item[1] for item in cmds], 'cmd_times': [item[2] for item in cmds]})
        # cmds =getattr(Cmd,ip_db).with_entities(Cmd.nbuf, Cmd.now, Cmd.time).filter(Cmd.now>offset).order_by(Cmd.now).limit(200).all()
        # return jsonify({'cmd_nbufs': [item.nbuf for item in cmds], 'cmd_nows': [item.now for item in cmds], 'cmd_times': [item.time for item in cmds]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
    # return jsonify({'cmd': [item.now&mask for item in cmds]})

# get the length of cmd now list

@api.route('/<ip_db>/cmd/<nbuf>')
# @cache.cached(timeout=3600)
def get_cmd(ip_db, nbuf):

    ## This will print a value into the command prompt with the first nbuf value that works
    # print "---------------- getattr >"
    # print getattr(Cmd,ip_db).first().nbuf
    # print "---------------- getattr <"
    try:
        cmd =getattr(Cmd,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'cmd': cmd.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
