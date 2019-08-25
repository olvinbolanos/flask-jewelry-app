import models

import os
import sys
import secrets
from PIL import Image

from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from playhouse.shortcuts import model_to_dict

client = Blueprint('clients', 'client', url_prefix='/client')


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

@client.route('/', methods=['POST'])
def create_client(): #this is similar to the register route
    print(request)
    print(type(request))

    pay_file = request.files
    payload = request.form.to_dict()
    dict_file = pay_file.to_dict()
    file_picture_path = save_picture(dict_file['file'])

    payload['image'] = file_picture_pathclient = models.Client.create(**payload)
    print(type(client))
    current_user.image  = file_picture_pathuser_dict = model_to_dict(client)
    print(user_dict)
    print(type(user_dict))
    return jsonify(data=user_dict, status={"code": 201, "message": "Success"})


