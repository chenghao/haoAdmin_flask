# coding:utf-8

from flask import request
from flask.ext.login import current_user
from utils import templated, cached, jsonify
from dal import haoAdmin
from utils.route import FlaskBlueprint as Blueprint

admin = Blueprint('admin', __name__)
from handler.haoAdmin import auth, home, menu, type, user

__author__ = "chenghao"


@admin.route("/")
@templated("haoAdmin/index")
@cached()
def index():
    # 用户id
    user_id = current_user.get_id()

    result = haoAdmin.get_main_menu(user_id=user_id)

    return result


@admin.route("/get_main_menu")
@cached()
def get_main_menu():
    # 用户id
    user_id = current_user.get_id()
    menu_id = request.values.get("menu_id", "")

    result = haoAdmin.get_main_menu(user_id=user_id, parent_menu_id=menu_id)

    return jsonify(result=result)
