# coding:utf-8

from flask import Blueprint, request, jsonify
from flask.ext.login import current_user
from utils import templated, cached
from dal import haoAdmin

__author__ = "chenghao"

admin = Blueprint('admin', __name__)


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
