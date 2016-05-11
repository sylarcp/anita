from flask import render_template, session, redirect, url_for, current_app
# from ..models import User
from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/trigmon', methods=['GET'])
def trigmon():
    return render_template('trigmon.html')

@main.route('/slowmo', methods=['GET'])
def slowmo():
    return render_template('slowmo.html')
