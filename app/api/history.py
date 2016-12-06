from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Hd, Wv, Hk, Mon, Adu5_pat, Adu5_vtg, Adu5_sat,G12_pos, G12_sat,Turf, Hk_surf, Slow, Sshk


@api.route('/<ip_db>/history/<table_name>/<column_name>/<start_time>/<end_time>')
def get_history(ip_db, table_name, column_name, start_time, end_time):
    try:
        # dict = {'Hd':Hd, 'Wv':Wv, 'Hk':Hk, 'Mon':Mon, 'Adu5_sat':Adu5_sat, 'Adu5_vtg':Adu5_vtg, 'Adu5_pat':Adu5_pat, 'Sshk':Sshk, 'Turf':Turf, 'Hk_surf':Hk_surf}
        diction = {'hd':Hd, 'wv':Wv, 'hk':Hk, 'mon':Mon, 'adu5_sat':Adu5_sat, 'adu5_vtg':Adu5_vtg, 'adu5_pat':Adu5_pat, 'g12_pos':G12_pos, 'g12_sat':G12_sat, 'sshk': Sshk,'turf':Turf, 'hk_surf':Hk_surf, 'slow': Slow}
        # print column_name[-10:-7]
        if table_name == 'gps':
            if column_name[-10:-7] == 'adu':
                # adu5 case
                if column_name[-1] == 'A':
                    gpstype = 0x20000
                else:
                    gpstype = 0x40000
                table_name = column_name[-10:-2]
                column_name = column_name[:-11]
                
            else:
                # g12 case
                table_name = column_name[-7:]
                column_name = column_name[:-8]
            if column_name == 'unixtime':
                column_name = 'time'
            elif column_name == 'unixnow':
                column_name = 'now'
        # print table_name, column_name
        table = diction[table_name]
        if column_name[:3] == 'adu':
            results =getattr(table,ip_db).with_entities(getattr(table,column_name), table.time).filter(table.time>=start_time, table.time<=end_time, table.gpstype == gpstype).order_by(table.time).all()
        elif '-' in column_name:
            splited = column_name.split('-')
            column_name=splited[0]
            # slowmo rfpower, avgscaler
            if column_name in ['avgscaler', 'avgrfpow'] and len(splited) == 3:
                column_id1 = int(splited[1])
                column_id2 = int(splited[2])
                results =getattr(table,ip_db).with_entities(getattr(table,column_name), table.time).filter(table.time>=start_time, table.time<=end_time).order_by(table.time).all()
                return jsonify({'data':[[1000*result.time ,getattr(result, column_name)[column_id2][column_id1]] for result in results]})
            column_id=int(splited[1])
            # sshk info
            if column_id in [4,5,6,7] and column_name in ['ssaz', 'ssel', 'ssflag']:
                column_id = column_id - 4
                table = diction['sshk']
            results =getattr(table,ip_db).with_entities(getattr(table,column_name), table.time).filter(table.time>=start_time, table.time<=end_time).order_by(table.time).all()
            # print [[result.time, getattr(result, column_name)[column_id]] for result in results]
            return jsonify({'data':[[1000*result.time ,getattr(result, column_name)[column_id]] for result in results]})
        else:
            results =getattr(table,ip_db).with_entities(getattr(table,column_name), table.time).filter(table.time>=start_time, table.time<=end_time).order_by(table.time).all()
        # print results
            # print [[result.time, getattr(result, column_name)] for result in results]
            # slow: rate1, rate10 calibrition factor.
            if table_name == 'slow' and column_name in ['rate1', 'rate10']:
                return jsonify({'data':[[1000*result.time ,0.5 * getattr(result, column_name)] for result in results]})
            return jsonify({'data':[[1000*result.time ,getattr(result, column_name)] for result in results]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})