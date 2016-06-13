from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Adu5_pat, Adu5_vtg, Adu5_sat



@api.route('/<ip_db>/adu5/<now>')
def get_adu5(ip_db, now):
    print ""
    print getattr(Adu5_pat,ip_db).first().now
    adu5_pat =getattr(Adu5_pat,ip_db).filter_by(now=now).first()
    adu5_sat =getattr(Adu5_sat,ip_db).filter_by(now=now).first()
    adu5_vtg =getattr(Adu5_vtg,ip_db).filter_by(now=now).first()
    json_comment={}
    if adu5_pat == None:
        json_comment['pat']=''
    else:
        json_comment['pat']=adu5_pat.to_json()

    if adu5_vtg == None:
        json_comment['vtg']=''
    else:
        json_comment['vtg']=adu5_vtg.to_json()

    if adu5_sat == None:
        json_comment['sat']=''
    else:
        json_comment['sat']=adu5_sat.to_json()
    # return jsonify({'pat':adu5_pat.to_json(), 'vtg':adu5_vtg.to_json(), 'sat':adu5_sat.to_json()})
    return jsonify(json_comment)

