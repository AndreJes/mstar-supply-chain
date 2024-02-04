from flask import Blueprint, jsonify, request, Response
from services import CommodityTypeService as service_class
from models import CommodityType as model

bp = Blueprint('commodity_type', __name__, url_prefix="/commodity-types")

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

@bp.route("/<name>", methods=["GET"])
def get(name):
    results = service.get(name)
    return jsonify(results)

@bp.route("/<name>", methods=["PATCH"])
def update(name):
    body = request.get_json()
    results = service.update(name, body)
    return jsonify(results)

@bp.route("/<name>", methods=["DELETE"])
def delete(name):
    results = service.delete(name)
    return Response(None, status=204)