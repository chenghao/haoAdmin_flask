# coding:utf-8
from models import HMenu, HOrg, HRole, HUser
from peewee import JOIN_INNER, fn

__author__ = "chenghao"


def init_menus(user_id):
    """
    用户登录时获取当前用户的菜单数据集
    :param user_id:     用户id
    :return:
    """

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
    ).where(
        HUser.pid == user_id
    ).order_by(HMenu.parent_menu, HMenu.sort)

    result = [f for f in sql.dicts()]
    level_1_menus = []  # 一级菜单集合
    level_2_menus = {}  # 二级菜单集合
    level_1_child_key = "menu_%s"

    for res in result:
        if res["parent_menu"]:
            menus = level_2_menus[level_1_child_key % res["parent_menu"]]
            menus.append(res)
            level_2_menus[level_1_child_key % res["parent_menu"]] = menus
        else:
            level_2_menus[level_1_child_key % res["pid"]] = []
            level_1_menus.append(res)

    return {"level1": level_1_menus, "level2": level_2_menus}

