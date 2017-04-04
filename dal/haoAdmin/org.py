# coding:utf-8

from models import HOrg, HUser
from peewee import fn
from dal.haoAdmin import query_original_sql


def get_org_by_user_id(user_id):
    """
    根据用户id获取相关机构
    :param user_id:
    :return:
    """
    sql = """
        SELECT group_concat(t1.pid) AS org_ids, group_concat(t1.name) AS org_names
        FROM h_org AS t1
        INNER JOIN h_user AS t2 ON (t2.org_ids LIKE CONCAT('%%,', t1.pid, ',%%'))
        WHERE (t2.pid = %s)
    """
    result = query_original_sql(sql, (user_id, ))
    if result:
        result = result[0]
        return result
    else:
        return ""

