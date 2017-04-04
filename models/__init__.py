# coding:utf-8

from peewee import Model, PrimaryKeyField, DateTimeField, CharField, ForeignKeyField, IntegerField, TextField
from playhouse.pool import PooledMySQLDatabase
import conf
from flask.ext.login import UserMixin

__author__ = "chenghao"

database = PooledMySQLDatabase(conf.mysql_db,
                               user=conf.mysql_user, passwd=conf.mysql_passwd,
                               host=conf.mysql_host, port=conf.mysql_port,
                               max_connections=conf.mysql_max_connections,
                               stale_timeout=conf.mysql_stale_timeout)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    pid = PrimaryKeyField()
    create_time = DateTimeField(null=True)

    class Meta:
        database = database


class HMenu(BaseModel):
    """
    菜单表
    """
    icon = CharField(null=True)  # 图标
    level = IntegerField()  # 等级
    menu_name = CharField()  # 菜单名称
    menu_url = CharField(null=True)  # 菜单URL地址
    parent_menu = ForeignKeyField('self', null=True, related_name='children', db_column="parent_menu")  # 上级菜单
    sort = IntegerField()  # 菜单排序
    org_ids = TextField(null=True)  # 菜单所属机构
    role_ids = TextField(null=True)  # 菜单所属角色

    class Meta:
        db_table = 'h_menu'


class HOrg(BaseModel):
    """
    机构表
    """
    name = CharField()  # 机构名称
    description = CharField(null=True)  # 机构描述
    parent_org = ForeignKeyField('self', null=True, related_name='children', db_column="parent_org")  # 上级机构

    class Meta:
        db_table = 'h_org'


class HRole(BaseModel):
    """
    角色表
    """
    role_name = CharField()  # 角色名称
    role_code = CharField()  # 角色代码

    class Meta:
        db_table = 'h_role'


class HUser(BaseModel, UserMixin):
    """
    用户表
    """
    login_name = CharField(unique=True)  # 登录名称
    login_pwd = CharField()  # 登录密码
    user_name = CharField()  # 用户名称
    phone = CharField(null=True)  # 用户手机号
    sex = IntegerField(null=True)  # 用户性别
    org_ids = TextField(null=True)  # 用户所属机构
    role_ids = TextField(null=True)  # 用户所属角色

    class Meta:
        db_table = 'h_user'

    def get_id(self):
        return self.pid


class HType(BaseModel):
    create_time = DateTimeField(null=True)
    group = IntegerField(db_column='group_id')
    type_name = CharField()
    type_value = CharField()

    class Meta:
        db_table = 'h_type'


class HTypegroup(BaseModel):
    create_time = DateTimeField(null=True)
    group_name = CharField()
    group_value = CharField(unique=True)

    class Meta:
        db_table = 'h_typegroup'
