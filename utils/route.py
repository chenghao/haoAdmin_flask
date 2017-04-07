# coding:utf-8

from flask import Blueprint
import utils

log = utils.singletons.Log()


class FlaskBlueprint(Blueprint):
    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            try:
                self.add_url_rule(rule, endpoint, f, **options)
                return f
            except Exception as e:
                log.error(e.message, exc_info=True)
                return utils.jsonify(code=-1, msg=u"操作失败，%s" % e.message, ensure_ascii=False)
        return decorator


