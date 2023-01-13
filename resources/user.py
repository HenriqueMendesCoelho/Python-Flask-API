from flask import Blueprint, jsonify, request

from models.user import UserModel

user_bp = Blueprint('core', __name__)


# For URL query parameters, use request.args

# For body json parameters use request.json

@user_bp.route('/user/teste',  methods=['POST'])
def create_user():
    body = request.json
    body['id'] = None
    user = UserModel(**body)
    user.save_user()
    return user.json(), 200


@user_bp.route('/user',  methods=['GET'])
def get_user_by_id():
    id = request.args.get('id')
    user = UserModel.find_user_by_id(id)

    if user:
        return user.json(), 200
    return jsonify(message='user not foud'), 404
