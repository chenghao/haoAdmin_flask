# coding:utf-8

import conf
from models import HUser, HType
import operator


def get_users(page, user_id, page_row=conf.ROWS, role_codes=None, **kv):
    """
    获取用户
    :param page:
    :param page_row:
    :param kv:
    :return:
    """
    # 判断当前用户是不是管理员
    if conf.ROLE_CODE_ADMIN in role_codes:  # 是管理员
        sql = HUser.select(

        ).join(

        )
    else:
        return [], 0
