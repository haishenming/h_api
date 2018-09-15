from flask import Blueprint

from app.api.v1 import user
from app.api.v1 import book


def create_blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)

    # 红图向蓝图注册
    user.api.register(bp_v1)
    book.api.register(bp_v1)
