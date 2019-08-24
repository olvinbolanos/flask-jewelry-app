import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

api = Blueprint('api', 'api', url_prefix="/api/v1")

@api.route('/', methods=["GET"])
def get_all_clients():
    print("HITTING THE GET CLIENT ROUTE!!!!!")
    try:
        clients = [model_to_dict(client) for client in models.Client.select()]
        return jsonify(data=clients, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})

@api.route('/', methods=["POST"])
def create_clients():
    payload = request.get_json()
    print(payload, 'payload', type(payload), 'type')

    client = models.Client.create(**payload, user=1) #I will be changing this to a generated key
    print(client.__dict__, ' looking inside the client model', type(client))

    client_dict = model_to_dict(client)

    return jsonify(data=client_dict, status={"code": 201, "message": "Success"})

# show route
@api.route('/<id>',  methods=["GET"])
def get_one_client(id):
    client = models.Client.get_by_id(id)
    return jsonify(data=model_to_dict(client), status={"code": 200, "message": "Success"})

# update client
@api.route('/<id>', methods=["PUT"])
def update_client(id):
    payload = request.get_json()

    query = models.Client.update(**payload).where(models.Client.id == id)
    query.execute()

    updated_client = models.Client.get_by_id(id)
    return jsonify(data=model_to_dict(updated_client), status={"code": 200, "message": "Success"})

# delete client
@api.route('/<id>', methods=["DELETE"])
def delete_client(id):
    query = models.Client.delete().where(models.Client.id == id)
    query.execute()

    return jsonify(data='resources successfully deleted', status={"code": 200, "message": "message resources deleted"})

