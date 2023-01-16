import time

from flask import Blueprint

handler = Blueprint('errors', __name__)


@handler.app_errorhandler(404)
def handle_404(err):
    return {"code": 404,
            "message": err.description,
            "timestamp": time.time()}, 404


@handler.app_errorhandler(500)
def handle_500(err):
    return {"code": 500,
            "message": "Internal server error - contact administrator",
            "timestamp": time.time()}, 500
