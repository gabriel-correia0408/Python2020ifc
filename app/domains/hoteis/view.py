from app.config import *
from flask import request, jsonify
from app.domains.hoteis.actions import get as get_hoteis


@app.route("/")
def inicio():
    return "Bem vindo ao backend"


@app.route("/hoteis", methods=['GET'])
def get():
    query = request.args
    hoteis = get_hoteis(query)
    return jsonify
