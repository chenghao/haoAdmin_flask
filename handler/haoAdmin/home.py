# coding:utf-8

from utils import templated
from handler.haoAdmin import admin


@admin.route("/home")
@templated("haoAdmin/home/index")
def home():
    return {}
