from flask import request, jsonify

from app.app import *
from app.domains.hoteis.actions import get as get_hoteis, create as create_hoteis
from app.domains.hoteis.schema import HoteisSchema

_HOTEIS_SCHEMA = HoteisSchema


@app.route("/")
def inicio():
    return "Bem vindo ao backend"


@app.route("/buscarhoteis", methods=['GET'])
def get():
    query = request.args
    hoteis = get_hoteis(query)
    return jsonify(_HOTEIS_SCHEMA.dump(hoteis))


@app.route("/postarhoteis", methods=['POST'])
def post():
    payload = request.get_json()
    hoteis = create_hoteis(payload)
    return _HOTEIS_SCHEMA.dump(hoteis), 201
