from flask import Blueprint, jsonify
from flask_restful import Resource, reqparse

hoteis = [{'id': 1, 'nome': 'HotelSFS', 'cidade': 'São Paulo'}]


hotel_bp = Blueprint('core', __name__)


@hotel_bp.route('/teste-bp',  methods=['GET'])
def index():
    return jsonify({"mensagem": "OK"}), 201


class Hoteis(Resource):
    def get(self):
        return hoteis


class GetUpdateHotel(Resource):
    def get(self, id):
        for hotel in hoteis:
            if hotel['id'] == id:
                return hotel


class CreateHotel(Resource):
    def post(self):
        bodyParams = reqparse.RequestParser()
        bodyParams.add_argument('id')
        bodyParams.add_argument('nome')
        bodyParams.add_argument('cidade')

        body = bodyParams.parse_args()
        body.id = int(body.id)
        hoteis.append(body)

        return body, 200
