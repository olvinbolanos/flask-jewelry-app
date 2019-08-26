import models

import os
import sys
import secrets
from PIL import Image

from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required
from flask import Flask 

from playhouse.shortcuts import model_to_dict

api = Blueprint('api', 'api', url_prefix="/api/v1")

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + f_ext
    file_path_for_avatar = os.path.join(os.getcwd(), 'static/profile_pics/' + picture_name)
    output_size = (125, 175)

    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(file_path_for_avatar)

    return picture_name

@api.route('/', methods=["POST"])
def create_clients():
    print(request)
    print(type(request))
   
    pay_file = request.files
    payload = request.form.to_dict()
    dict_file = pay_file.to_dict()
    file_picture_path = save_picture(dict_file['file'])
    payload['image'] = file_picture_path
    client = models.Client.create(**payload, user = current_user.get_id()) 
    print(client.__dict__, ' looking inside the client Model', type(client))

    client_dict = model_to_dict(client)
    print(type(client_dict))

    return jsonify(data=client_dict, status={"code": 201, "message": "Success"})

@api.route('/', methods=["GET"])
def get_all_clients():
    print("HITTING THE GET CLIENT ROUTE!!!!!")
    try:
        clients = [model_to_dict(client) for client in models.Client.select()]
        return jsonify(data=clients, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})


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

