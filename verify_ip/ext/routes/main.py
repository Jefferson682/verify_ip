from flask import Blueprint
from verify_ip.ext.controllers.verify_ip import select_ip, verify_ip

bp = Blueprint("routes", __name__)

@bp.route('/')
def index():
    return "Hello API"

@bp.route('/verify')
def verify():
    return verify_ip(select_ip())