# coding:utf-8

import conf
from dal.haoAdmin import query_original_sql


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
        sql = """
            select t1.pid, t1.login_name, t1.user_name, ifnull(t1.phone, '') as phone,
            ifnull(t1.sex, '') as sex, DATE_FORMAT(t1.create_time, '%%Y-%%m-%%d %%H:%%i') as create_time
            from h_user as t1
            inner join h_org as t2 on t1.org_ids like CONCAT('%%,', t2.pid, ',%%')
            inner join (
                SELECT org_ids
                from h_user where pid=%s
            ) as t3 on t3.org_ids like CONCAT('%%,', t2.pid, ',%%')
            where t1.login_name like concat('%%', %s, '%%')
              or t1.user_name like concat('%%', %s, '%%')
              or t1.phone like concat('%%', %s, '%%')
            GROUP by t1.pid
        """

        keyword = kv["keyword"]

        sql_count = "select count(1) as rows from( %s ) as t" % sql
        counts = query_original_sql(sql_count, (user_id, keyword, keyword, keyword))
        count = 0
        if counts:
            count = counts[0]["rows"]

        sql += " limit %s, %s "
        result = query_original_sql(sql, (user_id, keyword, keyword, keyword, ((page - 1) * page_row), page_row))
        return result, count
    else:
        return [], 0
