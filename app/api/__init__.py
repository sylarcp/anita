from flask import Blueprint
api = Blueprint('api', __name__)
from . import session, hd, slow, wv