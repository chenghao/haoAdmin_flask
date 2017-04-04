# coding:utf-8

from flask import Blueprint
from utils import templated

main = Blueprint('main', __name__)


@main.route("/")
@templated("haoAdmin/main")
def index():
    return {}
