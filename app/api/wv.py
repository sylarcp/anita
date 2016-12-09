from flask import jsonify, request, g, abort, url_for, current_app, session, Response
from . import api
from .. import cache
from app.models import Wv


#Primary key list: get the (evnum, id)
@api.route('/<ip_db>/wv/evnum_ids')
def get_wv_evnum_ids(ip_db):
    try:
        wvs =getattr(Wv,ip_db).limit(1000).all()
        return jsonify({'wv': [(item.evnum, item.id) for item in wvs]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

#get the length of wv list
@api.route('/<ip_db>/wv/count') 
def get_wv_count(ip_db):
    try:
        #Todo how to make it count fast?
        count =getattr(Wv,ip_db).count()
        # could not return long type, so use str()
        return str(count)
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

#get wv table content for evnum and id
@api.route('/<ip_db>/wv/<int:evnum>/<int:id>')
# @cache.cached(timeout=3600)
def get_wv(ip_db, evnum, id):
    try:
        wv =getattr(Wv,ip_db).filter_by(evnum=evnum, id=id).first()
        return jsonify({'wv': wv.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

#get 40 waveforms for a evnum
@api.route('/<ip_db>/wv/<int:evnum>')
# @cache.cached(timeout=3600)
def get_wvs(ip_db, evnum):
    try:
        json_comment={}
        wvs =getattr(Wv,ip_db).filter_by(evnum=evnum).order_by(Wv.id).all()
        json_comment['evnum'] = wvs[0].evnum
        # print type(wvs[0].evnum)
        # print type(wvs[0].cal[0])
        # print type(wvs[0].to_json()['cal'][0])
        for wv in wvs:
            json_comment[wv.id]=wv.to_json()
            # json_comment[wv.id + 100]=wv.to_json()
        return jsonify(json_comment)
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        return jsonify

#get averaged 40 waveforms for a time range.
@api.route('/<ip_db>/avgwv/<int:starttime>/<int:endtime>/<int:limitNum>')
# @cache.cached(timeout=3600)
def get_avgwvs(ip_db, starttime, endtime, limitNum):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Wv,engine_ip_db)
        evnums = engine.execute('SELECT evnum FROM rf WHERE time>=' + str(starttime) + ' AND time<=' + str(endtime) + 'ORDER BY time DESC LIMIT '+ str(limitNum) + ';').fetchall()
        
        json_comment={}
        count = 0
        # print evnums
        for evnum in evnums:
            wvs =getattr(Wv,ip_db).filter_by(evnum=evnum[0]).order_by(Wv.id).all()
            # print wvs
            if count == 0:
                last_evnum = evnum[0]
            for wv in wvs:
                if wv.id not in json_comment:
                    json_comment[wv.id]=wv.to_json()
                else:
                    sumed_wv = json_comment[wv.id]
                    current_wv = wv.to_json()
                    new_wv = [x + y for x, y in zip(sumed_wv['cal'], current_wv['cal'])]
                    sumed_wv['cal'] = new_wv
                    json_comment[wv.id] = sumed_wv
                # json_comment[wv.id + 100]=wv.to_json()
            count += 1
        first_evnum = evnum[0]
        if count:
            for id in json_comment:
                # print id
                # print json_comment[id]
                json_comment[id]['cal'] = [sumed_mv/count for sumed_mv in json_comment[id]['cal']]
            json_comment['evnum'] = last_evnum
        json_comment['count'] = count
        json_comment['first_evnum'] = first_evnum
        return jsonify(json_comment)
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        return jsonify({})