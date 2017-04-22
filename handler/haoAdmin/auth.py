# coding:utf-8
from flask import render_template, request, session
from flask.ext.login import login_user, logout_user, current_user
from peewee import DoesNotExist
import conf, utils
from dal.haoAdmin import org as org_dal
from dal.haoAdmin import role as role_dal
from models import HUser
from utils.singletons import Cache
from utils import jsonify
from handler.haoAdmin import admin

__author__ = "chenghao"

log = utils.singletons.Log()


@admin.route("/auth/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('haoAdmin/auth/login.html')
    else:
        login_name = request.form.get("login_name")
        login_pwd = request.form.get("login_pwd", "")
        remember_me = request.form.get("rememberMe", None)
        remember_me = True if remember_me == "true" else False

        try:
            user = HUser.get(HUser.login_name == login_name, HUser.login_pwd == utils.get_md5_s(login_pwd))
            if user:
                # 获取相关机构
                org = org_dal.get_org_by_user_id(user.pid)
                if org:
                    session["user_org"] = org
                # 获取相关角色
                role = role_dal.get_role_by_user_id(user.pid)
                if role:
                    session["user_role"] = role

                user.login_pwd = None
                login_user(user, remember_me)

                return jsonify(code=0)
        except DoesNotExist as e:
            log.error(e.message, exc_info=True)
            return jsonify(code=-1, msg="用户名或密码错误", ensure_ascii=False)


@admin.route('/auth/logout', methods=['POST'])
def logout():
    try:
        user_id = current_user.get_id()
        logout_user()

        # 清空当前用户相关的session
        session.clear()

        # 清空当前用户相关的cache
        cache = Cache()
        key = "%s%s" % (conf.cache_redis_prefix, user_id)
        cache.clear(key_prefix=key)

        return jsonify(code=0)
    except Exception as e:
        log.error(e.message, exc_info=True)
        return jsonify(code=-1, msg="退出失败", ensure_ascii=False)