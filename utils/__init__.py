# coding:utf-8

import hashlib, base64, re, uuid, json
from datetime import datetime, date
import conf
from functools import wraps
from flask import request, render_template, current_app
from flask.json import dumps
from flask.ext.login import current_user
from utils import singletons

__author__ = "chenghao"

__all__ = [
    "singletons"
]


def get_format_date(pattern="%Y-%m-%d %H:%M:%S", datetime_s=None):
    """
    格式化日期
    :param pattern:
    :param datetime_s:
    :return:
    """
    if datetime_s is None:
        result = datetime.now().strftime(pattern)
    elif isinstance(datetime_s, datetime):
        result = datetime_s.strftime(pattern)
    elif isinstance(datetime_s, date):
        result = datetime_s.strftime("%Y-%m-%d")
    else:
        result = datetime_s
    return result


def ver_mobile(data):
    """
    验证手机号，正确返回True
    :param data:
    :return:
    """
    p = re.compile(r"((13|14|15|17|18)\d{9}$)")
    return p.match(data)


def ver_email(data):
    """
    验证邮箱，正确返回True
    :param data:
    :return:
    """
    p = re.compile(r"(\w+[@]\w+[.]\w+)")
    return p.match(data)


def random_num():
    """
    获取随机数
    :return:
    """
    return uuid.uuid4().hex.lower()


class ComplexEncoder(json.JSONEncoder):
    """
    json日期格式化
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def get_md5_s(s, salt="haoAdmin"):
    """
    MD5加密
    :param s: 需要加密的字符串
    :param salt:  盐
    :return:  加密后的字符串
    """
    if s == "":
        return ""
    md5code = hashlib.md5(s.encode()).hexdigest()[8:10]
    key = hashlib.md5(salt.encode()).hexdigest()
    len_key = len(key)
    _code = ""
    for i in range(len(s)):
        k = i % len_key
        # 先转为ascii在进行 ^ 运算
        _s = ord(s[i])
        _key = ord(key[k])

        _code += str(_s ^ _key)

    _encode = base64.b64encode(_code.encode("utf8"))
    _code = _encode.decode() + md5code
    return _code


def total_page(total_rows, rows=conf.ROWS):
    """
    将总行数计算出多少页
    """
    return int((total_rows - 1) / rows + 1)


###################################################################################################
def dict_cursor(cursor):
    column_names = [d[0] for d in cursor.description]
    return [_Row(zip(column_names, row)) for row in cursor]


class _Row(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


###################################################################################################
def jsonify(*args, **kwargs):
    indent = None
    separators = (',', ':')

    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not request.is_xhr:
        indent = 2
        separators = (', ', ': ')

    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs

    ensure_ascii = False
    if kwargs.has_key("ensure_ascii"):
        ensure_ascii = kwargs.pop("ensure_ascii")

    return current_app.response_class(
        (dumps(data, indent=indent, separators=separators, ensure_ascii=ensure_ascii), '\n'),
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    )


def templated(template=None):
    """
    模版装饰器
    :param template:
    :return:
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            else:
                if ".html" not in template_name:
                    template_name += ".html"

            try:
                ctx = f(*args, **kwargs)
                ctx = {} if ctx is None else ctx
                if isinstance(ctx, dict):
                    return render_template(template_name, **ctx)
                else:
                    return render_template(template_name, result=ctx)
            except BaseException as e:
                log = singletons.Log()
                log.error(e.message, exc_info=True)
                return jsonify(code=-1, msg=u"操作失败，%s" % e.message, ensure_ascii=False)

        return decorated_function

    return decorator


def cached(timeout=5 * 60, key='view/%s'):
    """
    缓存装饰器
    :param timeout:
    :param key:
    :return:
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache = singletons.Cache()
            _key = "%s/%s/%s" % (current_user.get_id(), key, request.query_string)
            cache_key = _key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv

        return decorated_function

    return decorator


if __name__ == "__main__":
    print get_md5_s("111111")
