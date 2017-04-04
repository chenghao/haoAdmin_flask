# coding:utf-8
from models import HMenu, HOrg, HRole, HUser, database
from peewee import JOIN_INNER, fn
import utils
import operator

__author__ = "chenghao"


def get_main_menu(user_id, parent_menu_id=None):
    """
    主页获取菜单
    :param user_id:
    :param parent_menu_id:
    :return:
    """
    where_param = [HUser.pid == user_id]
    if parent_menu_id:
        where_param.append(HMenu.parent_menu == parent_menu_id)
    else:
        where_param.append(HMenu.parent_menu.is_null())
    and_conditions = reduce(operator.and_, where_param)

    sql = HMenu.select(
        HMenu.pid, HMenu.menu_name.alias("title"), HMenu.menu_url.alias("href"), HMenu.parent_menu, HMenu.icon
    ).join(
        HOrg, join_type=JOIN_INNER, on=HMenu.org_ids ** (fn.CONCAT("%,", HOrg.pid, ",%"))
    ).join(
        HRole, join_type=JOIN_INNER, on=HMenu.role_ids ** (fn.CONCAT("%,", HRole.pid, ",%"))
    ).join(
        HUser, join_type=JOIN_INNER,
        on=((HUser.org_ids ** (fn.CONCAT("%,", HOrg.pid, ",%"))) &
            (HUser.role_ids ** (fn.CONCAT("%,", HRole.pid, ",%"))))
    ).where(and_conditions).group_by(HMenu.pid).order_by(HMenu.pid, HMenu.sort)

    result = [f for f in sql.dicts()]
    return result


def query_original_sql(sql, params):
    """
    原生sql查询
    :param sql:
    :param params:
    :return:
    """
    cursor = database.execute_sql(sql, params)
    res = utils.dict_cursor(cursor)
    return res
