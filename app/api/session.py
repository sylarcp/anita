from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api

# store current user's session info

@api.route('/session/<ip>/<db>')
def set_session_info(ip, db):
    session['ip'] = ip
    session['db'] = db
    session['ip_db']= 'query_'+ip+'_'+db
    return 'Success', 200
