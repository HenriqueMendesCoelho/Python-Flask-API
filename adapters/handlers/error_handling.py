import time

from flask import Blueprint, jsonify, make_response
from jsonschema import ValidationError

handler = Blueprint('errors', __name__)


@handler.app_errorhandler(400)
def handle_404(err):
    if isinstance(err.description, ValidationError):
        original_error = err.description
        return make_response(jsonify({'error': original_error.message}), 400)
    return err


@handler.app_errorhandler(500)
def handle_500(err):
    return {"code": 500,
            "message": "Internal server error - contact administrator",
            "timestamp": time.time()}, 500
