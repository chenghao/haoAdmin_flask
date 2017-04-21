# coding:utf-8

from utils import templated
from utils.route import FlaskBlueprint as Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@templated("haoAdmin/main/index")
def index():
    return {}
