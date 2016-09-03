
from flask import Blueprint
api = Blueprint('api', __name__)
from . import connect, hd, slow, wv, hk, adu5, mon, history, turf, hk_surf, sshk, g12
