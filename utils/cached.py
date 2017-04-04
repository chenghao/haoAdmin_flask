# coding:utf-8

from werkzeug.contrib.cache import RedisCache


class RedisCached(RedisCache):

    def clear(self, key_prefix=None):
        status = False
        if self.key_prefix:
            keys = self._client.keys(key_prefix + '*')
            if keys:
                status = self._client.delete(*keys)
        else:
            status = self._client.flushdb()
        return status
