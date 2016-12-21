from flask import render_template, session, redirect, url_for, current_app, make_response, request
# from ..models import User
from sqlalchemy import create_engine
from . import main

# @main.route('/setDBlist/<ip>', methods=['GET'])
# def getDBlist(ip):
#     try:
#         engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') + '/template1', convert_unicode=True)
#         conn = engine.connect()
#         # rows = conn.execute("SELECT pg_database.datname, pg_database_size(pg_database.datname), pg_size_pretty(pg_database_size(pg_database.datname)) FROM pg_database ORDER BY pg_database_size DESC;")
#         rows = conn.execute("SELECT pg_database.datname FROM pg_database order by datname;")
#         dbnames_prev = []
#         dbnames = []
#         for row in rows:
#             if row["datname"][:7] == 'anita_1':
#                 dbnames_prev.append(row["datname"])
#             elif row["datname"][:7] == 'anita_0':
#                 dbnames.append(row["datname"])
#         dbnames= dbnames_prev + dbnames
#         return dbnames
#     except Exception as error:
#         print error
#         return None

    
   
@main.route('/', methods=['GET'])
def index():

    ip_selected = request.cookies.get('ip_selected') or '128.175.112.58'
    db_selected = request.cookies.get('db_selected') or 'anita_0102a'
    # db_list = getDBlist(ip_selected) or ['']
    # if len(db_list) == 1 and db_list[0] == '':
    #     db_selected = 'No results'

    resp = make_response(render_template('index.html', ip_selected=ip_selected, db_selected = db_selected))
    resp.set_cookie('username', 'pengcao')
    return resp

@main.route('/set_cookie/<ip_selected>/<db_selected>')
def cookie_insertion(ip_selected, db_selected):
    redirect_to_index = redirect('/hk')
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('ip_selected',ip_selected.replace('_','.'))
    response.set_cookie('db_selected',db_selected)
    print '!!!' + ip_selected
    print '!!!' + db_selected
    return response

@main.route('/trigmon', methods=['GET'])
def trigmon():
    ip_selected = request.cookies.get('ip_selected') or '128.175.112.58'
    db_selected = request.cookies.get('db_selected') or 'anita_0102a'
    # db_list = getDBlist(ip_selected) or ['']
    # if len(db_list) == 1 and db_list[0] == '':
    #     db_selected = 'No results'
    return render_template('trigmon.html', ip_selected=ip_selected,db_selected=db_selected)

@main.route('/slowmo', methods=['GET'])
def slowmo():
    ip_selected = request.cookies.get('ip_selected') or '128.175.112.58'
    db_selected = request.cookies.get('db_selected') or 'anita_0102a'
    # db_list = getDBlist(ip_selected) or ['']
    # if len(db_list) == 1 and db_list[0] == '':
    #     db_selected = 'No results'
    return render_template('slowmo.html', ip_selected=ip_selected,db_selected=db_selected)
@main.route('/hk', methods=['GET'])
def hk():
    ip_selected = request.cookies.get('ip_selected') or '128.175.112.58'
    db_selected = request.cookies.get('db_selected') or 'anita_0102a'
    # db_list = getDBlist(ip_selected) or ['']
    # if len(db_list) == 1 and db_list[0] == '':
    #     db_selected = 'No results'
    return render_template('hk.html', ip_selected=ip_selected,db_selected=db_selected)

@main.route('/hd', methods=['GET'])
def hd():
    ip_selected = request.cookies.get('ip_selected') or '128.175.112.58'
    db_selected = request.cookies.get('db_selected') or 'anita_0102a'
    # db_list = getDBlist(ip_selected) or ['']
    # if len(db_list) == 1 and db_list[0] == '':
    #     db_selected = 'No results'
    return render_template('hd.html', ip_selected=ip_selected,db_selected=db_selected)

@main.route('/gps', methods=['GET'])
def gps():
    ip_selected = request.cookies.get('ip_selected') or '128.175.112.58'
    db_selected = request.cookies.get('db_selected') or 'anita_0102a'
    # db_list = getDBlist(ip_selected) or ['']
    # if len(db_list) == 1 and db_list[0] == '':
    #     db_selected = 'No results'
    return render_template('gps.html', ip_selected=ip_selected,db_selected=db_selected)
    
@main.route('/contactus', methods=['GET'])
def contactus():
    return render_template('contactus.html')
