from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Hd, Wv, Hk, Mon, Adu5_pat, Adu5_vtg, Adu5_sat, Slow


@api.route('/<ip_db>/history/<table_name>/<column_name>/<start_time>/<end_time>')
def get_history(ip_db, table_name, column_name, start_time, end_time):
    try:
        # dict = {'Hd':Hd, 'Wv':Wv, 'Hk':Hk, 'Mon':Mon, 'Adu5_sat':Adu5_sat, 'Adu5_vtg':Adu5_vtg, 'Adu5_pat':Adu5_pat, 'Sshk':Sshk, 'Turf':Turf, 'Hk_surf':Hk_surf}
        diction = {'hd':Hd, 'wv':Wv, 'hk':Hk, 'mon':Mon, 'adu5_sat':Adu5_sat, 'adu5_vtg':Adu5_vtg, 'adu5_pat':Adu5_pat}
        table = diction[table_name]
        if '_' in column_name:
            splited = column_name.split('-')
            column_name=splited[0]
            column_id=int(splited[1])
            print column_name, column_id
            results =getattr(table,ip_db).with_entities(getattr(table,column_name), table.time).filter(table.time>=start_time, table.time<=end_time).order_by(table.time).all()
            print [[result.time, getattr(result, column_name)[column_id]] for result in results]
            return jsonify({'data':[[10000*result.time ,getattr(result, column_name)[column_id]] for result in results]})
        else:
            results =getattr(table,ip_db).with_entities(getattr(table,column_name), table.time).filter(table.time>=start_time, table.time<=end_time).order_by(table.time).all()
        # print results
            print [[result.time, getattr(result, column_name)] for result in results]
            return jsonify({'data':[[10000*result.time ,getattr(result, column_name)] for result in results]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})