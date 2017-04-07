# coding:utf-8
from flask import request, session
from flask.ext.login import current_user
from utils import templated, jsonify
from utils.route import FlaskBlueprint as Blueprint
import utils
from dal.haoAdmin import user as dal_user

__author__ = "chenghao"

user = Blueprint('user', __name__)


@user.route("/index")
@templated("haoAdmin/user/index")
def index():
    return {}


@user.route("/get_users")
def get_users():
    """
    获取用户列表
    :return:
    """
    page_no = int(request.values.get("page_no", 1))
    page = 0 if page_no < 1 else page_no
    keyword = request.values.get("keyword", "")

    user_id = current_user.get_id()  # 当前用户ID
    role = session["user_role"]
    role_codes = role["role_codes"] if role else None  # 当前用户角色

    results = dal_user.get_users(page, user_id, role_codes=role_codes, keyword=keyword)
    users = results[0]
    users_count = results[1]

    return jsonify(users=users, page_no=page_no, total_page=utils.total_page(users_count))
