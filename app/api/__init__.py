from flask import Blueprint
api = Blueprint('api', __name__)
from . import hd, slow, wv