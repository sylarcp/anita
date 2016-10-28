from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Cmd


@api.route('/<ip_db>/cmd/nbufs/<start_time>')
def get_cmd_nbufs(ip_db, start_time):
    try:
        cmds =getattr(Cmd,ip_db).with_entities(Cmd.nbuf, Cmd.now, Cmd.time).filter(Cmd.time>start_time).order_by(Cmd.now).all()
        return jsonify({'cmd_nbufs': [item.nbuf for item in cmds], 'cmd_nows': [item.now for item in cmds], 'cmd_times': [item.time for item in cmds]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
    # return jsonify({'cmd': [item.now&mask for item in cmds]})

# get the length of cmd now list

@api.route('/<ip_db>/cmd/<nbuf>')
@cache.cached(timeout=3600)
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
