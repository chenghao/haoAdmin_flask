# coding:utf-8

from models import HRole, HUser
from peewee import fn


def get_role_by_user_id(user_id):
    """
    根据用户id获取相关角色
    :param user_id:
    :return:
    """
    sql = HRole.select(
        fn.group_concat(HRole.role_code).alias("role_codes"),
        fn.group_concat(HRole.role_name).alias("role_names"),
    ).join(
        HUser, on=HUser.role_ids ** (fn.CONCAT("%,", HRole.pid, ",%"))
    ).where(HUser.pid == user_id)

    result = [f for f in sql.dicts()]
    if result:
        return result[0]

    return ""
