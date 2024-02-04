from flask import Blueprint, jsonify, request, Response
from services import ManufacturerService as service_class
from models import Manufacturer as model

bp = Blueprint('manufacturer', __name__, url_prefix="/manufacturers")

service = service_class()

@bp.route("/", methods=["GET"])
def list_all():
    results = service.list_all()
    return jsonify(results)

@bp.route("/", methods=["POST"])
def add():
    body = request.get_json()
    results = service.insert(model.from_dict(body))
    return jsonify(results)

@bp.route("/<cpf_cnpj>", methods=["GET"])
def get(cpf_cnpj):
    results = service.get(cpf_cnpj)
    return jsonify(results)

@bp.route("/<cpf_cnpj>", methods=["PATCH"])
def update(cpf_cnpj):
    body = request.get_json()
    results = service.update(cpf_cnpj, body)
    return jsonify(results)

@bp.route("/<cpf_cnpj>", methods=["DELETE"])
def delete(cpf_cnpj):
    results = service.delete(cpf_cnpj)
    return Response(None, status=204)