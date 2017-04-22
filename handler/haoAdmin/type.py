# coding:utf-8

from flask import request
import utils
from dal.haoAdmin import type as dal_type
from utils import templated, jsonify
from handler.haoAdmin import admin


@admin.route("/type/index")
@templated("haoAdmin/type/index")
def type():
    return {}


@admin.route("/type/get_typegroup")
def get_typegroup():
    """
    获取字典分类
    :return:
    """
    page_no = int(request.values.get("page_no", 1))
    page = 0 if page_no < 1 else page_no
    keyword = request.values.get("keyword", "")

    results = dal_type.get_typegroup(page, keyword=keyword)
    groups = results[0]
    groups_count = results[1]

    return jsonify(groups=groups, page_no=page_no, total_page=utils.total_page(groups_count))


@admin.route("/type/get_type")
def get_type():
    """
    根据分类id查询数据
    :return:
    """
    group_id = request.values.get("group_id")  # 字典分类id

    result = dal_type.get_type(group_id)
    return jsonify(types=result)
