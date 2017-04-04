# coding:utf-8
from flask import Blueprint, jsonify, request, session
from flask.ext.login import current_user

from dal.haoAdmin import menu as dal_menu
from utils import templated

__author__ = "chenghao"

menu = Blueprint('menu', __name__)


@menu.route("/index")
@templated("haoAdmin/menu/index")
def index():
    return {}


@menu.route("/get_parent_menu")
def get_parent_menu():
    user_id = current_user.get_id()  # 当前用户ID
    menu_id = request.args.get("menu_id", "")  # 菜单ID
    role = session["user_role"]
    role_codes = role["role_codes"] if role else None  # 当前用户角色
    is_children = request.values.get("is_children", "")  # 是否查询子菜单
    menus = dal_menu.get_menu(menu_id, user_id=user_id, role_codes=role_codes, is_children=is_children)
    return jsonify(menus=menus)

'''
@menu_app.get("/get_child_menu")
def get_child_menu():
    parent_id = request.params.getunicode("parent_id")

    cache_key = "menu_childMenu_" + parent_id
    ca = cache.get_cache(conf.cache_key, **conf.cache_opt)
    if cache_key in ca:
        two_level_menu = ca.get(cache_key)
    else:
        menus = haoAdmin.get_menu(parent_id=parent_id)
        two_level_menu = [r for r in menus.dicts()]
        ca.put(cache_key, two_level_menu)

    return {"two_level_menu": two_level_menu}
'''