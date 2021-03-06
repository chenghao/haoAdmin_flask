# coding:utf-8

from flask import Flask, request, redirect
from flask.ext.login import LoginManager, current_user
from flask_session import Session
from models import HUser
from handler.haoAdmin import admin
from datetime import timedelta
from peewee import DoesNotExist
import utils, conf
from conf import URL_PREFIX
from redis import Redis
from utils import jsonify

__author__ = "chenghao"
app = Flask(__name__, static_url_path=URL_PREFIX + '/static')

# flask-login
app.secret_key = 'haoAdmin_secret'
app.permanent_session_lifetime = timedelta(minutes=30)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.remember_cookie_duration = timedelta(minutes=30)
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# 设置redis为session存储
SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
SESSION_PERMANENT = False
SESSION_KEY_PREFIX = conf.session_redis_prefix
SESSION_REDIS = Redis(host=conf.redis_host, port=conf.redis_port, db=conf.session_redis_db,
                      password=conf.redis_password)
app.config.from_object(__name__)
Session(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return HUser.select().where(HUser.pid == user_id).get()
    except DoesNotExist as e:
        log = utils.singletons.Log()
        log.error(e.message, exc_info=True)
        return None


@app.before_request
def first_request():
    path_str = request.path

    if "/auth/login" not in path_str:
        pid = current_user.get_id()
        if not pid:
            if "/static" not in path_str:
                return redirect(URL_PREFIX + "/auth/login")
    return None


@app.errorhandler(422)
def handle_validation_error(err):
    exc = err.data['exc']
    return jsonify(errors=exc.messages), 422


@app.errorhandler(404)
def handle_404(err):
    return jsonify(errors=str(err)), 404


app.register_blueprint(admin, url_prefix=URL_PREFIX)
