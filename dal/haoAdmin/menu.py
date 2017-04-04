# coding:utf-8
from models import HMenu, HOrg, HRole, HUser
from peewee import JOIN_INNER, JOIN_LEFT_OUTER, fn
import operator
import conf


def get_menu(menu_id=None, user_id=None, role_codes=None, is_children=None):
    """
    获取菜单，menu_id为空时查询一级菜单，
    is_children为None时根据menu_id查询菜单信息，
    否则查询menu_id相关的子菜单
    :param menu_id:         菜单主键
    :param is_children:     是否是查询子菜单
    :param user_id:         当前用户ID
    :return:
    """
    Menu = HMenu.alias()
    ParentMenu = HMenu.alias()

    where_param = [HUser.pid == user_id]
    if is_children and menu_id:
        where_param.append(Menu.parent_menu == menu_id)
    elif menu_id:
        where_param.append(Menu.pid == menu_id)
    else:
        where_param.append(Menu.parent_menu.is_null())
    and_conditions = reduce(operator.and_, where_param)

    # 判断当前用户是不是管理员
    if conf.ROLE_CODE_ADMIN in role_codes:  # 是管理员
        sql = Menu.select(
            Menu.pid, Menu.menu_name, Menu.sort, HOrg.name.alias("org_name"), HRole.role_name,
            fn.ifnull(ParentMenu.menu_name, "").alias("parent_name"),
            fn.ifnull(Menu.menu_url, "").alias("menu_url")
        ).join(
            ParentMenu, join_type=JOIN_LEFT_OUTER, on=Menu.parent_menu == ParentMenu.pid
        ).join(
            HOrg, join_type=JOIN_INNER, on=Menu.org_ids ** (fn.CONCAT("%,", HOrg.pid, ",%"))
        ).join(
            HRole, join_type=JOIN_INNER, on=Menu.role_ids ** (fn.CONCAT("%,", HRole.pid, ",%"))
        ).join(
            HUser, join_type=JOIN_INNER,
            on=HUser.org_ids ** (fn.CONCAT("%,", HOrg.pid, ",%"))
        ).where(and_conditions).order_by(Menu.pid, Menu.sort)
    else:  # 不是管理员
        sql = Menu.select(
            Menu.pid, Menu.menu_name, Menu.sort, HOrg.name.alias("org_name"), HRole.role_name,
            fn.ifnull(ParentMenu.menu_name, "").alias("parent_name"),
            fn.ifnull(Menu.menu_url, "").alias("menu_url")
        ).join(
            ParentMenu, join_type=JOIN_LEFT_OUTER, on=Menu.parent_menu == ParentMenu.pid
        ).join(
            HOrg, join_type=JOIN_INNER, on=Menu.org_ids ** (fn.CONCAT("%,", HOrg.pid, ",%"))
        ).join(
            HRole, join_type=JOIN_INNER, on=Menu.role_ids ** (fn.CONCAT("%,", HRole.pid, ",%"))
        ).join(
            HUser, join_type=JOIN_INNER,
            on=((HUser.org_ids ** (fn.CONCAT("%,", HOrg.pid, ",%"))) &
                (HUser.role_ids ** (fn.CONCAT("%,", HRole.pid, ",%"))))
        ).where(and_conditions).order_by(Menu.pid, Menu.sort)

    result = [f for f in sql.dicts()]
    return result
