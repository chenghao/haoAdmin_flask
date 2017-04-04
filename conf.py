# coding:utf-8
__author__ = "chenghao"

URL_PREFIX = "/admin"  # URL前缀

ROWS = 1  # 每页显示条数

# mysql
mysql_db = "haoadmin"
mysql_user = "root"
mysql_passwd = "123456"
mysql_host = "localhost"
mysql_port = 3306
mysql_max_connections = 500
mysql_stale_timeout = 600

# log
log_path = "/home/chenghao/logs/haoAdmin_flask.log"
log_format = "%(asctime)s %(pathname)-5s %(funcName)-5s %(lineno)-5s %(levelname)-5s %(message)s"
log_level = "INFO"
log_when = "D"
log_interval = 1

# redis
redis_host = "127.0.0.1"
redis_port = 6379
redis_password = None
session_redis_db = 0
cache_redis_db = 1
session_redis_prefix = "session:"
cache_redis_prefix = "cache:"

# 角色code
ROLE_CODE_ADMIN = "admin"  # 管理员角色