from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json

from adapters.repositories.user_repository import UserRepository
from domain.user import UserModel

user_bp = Blueprint('core', __name__)


# For URL query parameters, use request.args

# For body json parameters use request.json


@user_bp.route('/user/<id>',  methods=['GET'])
def get_user_by_id(id):
    user = UserRepository().find_by_id(id)

    if user:
        return user.json(), 200
    return jsonify(message='User not foud'), 404


@user_bp.route('/user')
def list_users():
    users = UserRepository().list()

    if users:
        return [user.json() for user in users]
    return {}, 204


@ user_bp.route('/user',  methods=['POST'])
@expects_json({
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['name', 'email', 'password']
})
def create_user():
    body = request.json
    body['id'] = None
    user = UserModel(**body)
    UserRepository().save_and_flush(user)
    return user.json(), 200


@ user_bp.route('/user/<id>',  methods=['DELETE'])
def delete_user(id):
    user = UserRepository().find_by_id(id)
    if not user:
        return {}, 200

    UserRepository().delete_by_id(id)
    return {}, 200


@ user_bp.route('/user/<id>',  methods=['PUT'])
def update_user(id):
    user = UserRepository().find_by_id(id)
    if not user:
        return {"message": "user not foud"}, 404

    body = request.json
    user.id = id
    user.name = body['name']
    user.email = body['email']
    user.password = body['password']

    UserRepository().save_and_flush(user)
    return user.json(), 200
