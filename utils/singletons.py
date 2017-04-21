# coding:utf-8

import os, logging
from logging import handlers
import conf
from utils.cached import RedisCached

__author__ = "chenghao"


class SingletonLog(type):
    """
    日志单例
    """

    def __init__(cls, name, bases, dict):
        super(SingletonLog, cls).__init__(name, bases, dict)
        cls._instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            super(SingletonLog, cls).__call__(*args, **kwargs)
            # 按每天生成日志文件 linux
            file_path = conf.log_path
            parent_path = os.path.dirname(file_path)
            if not os.path.exists(parent_path):
                os.makedirs(parent_path)
            log_handler = handlers.TimedRotatingFileHandler(file_path, conf.log_when, conf.log_interval)
            # 格式化日志内容
            log_formatter = logging.Formatter(conf.log_format)
            log_handler.setFormatter(log_formatter)
            # 设置记录器名字
            log = logging.getLogger('haoAdmin')
            log.addHandler(log_handler)
            # 设置日志等级
            log.setLevel(conf.log_level)
            cls._instances = log
        return cls._instances


class Log(object):
    """
    获取log实例
    """
    __metaclass__ = SingletonLog


class SingletonCache(type):
    """
    缓存单例
    """

    def __init__(cls, name, bases, dict):
        super(SingletonCache, cls).__init__(name, bases, dict)
        cls._instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            super(SingletonCache, cls).__call__(*args, **kwargs)
            cls._instances = RedisCached(host=conf.redis_host, port=conf.redis_port, db=conf.cache_redis_db,
                                         password=conf.redis_password, key_prefix=conf.cache_redis_prefix)
        return cls._instances


class Cache(object):
    """
    获取缓存实例
    """
    __metaclass__ = SingletonCache


if __name__ == "__main__":
    # log = Log()
    # log.info("wwwwwwwwwwww")

    import time
    c = Cache()
    c.set("chenghao", "111222", timeout=20)
    print "%s ----" % c.get("chenghao")
    time.sleep(3)
    print "%s +++" % c.get("chenghao")
