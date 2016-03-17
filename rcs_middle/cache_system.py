# coding:UTF-8


"""
缓存系统核心模块
@author: yubang
"""


class CacheSystem(object):
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def use_cache(self, cache_key_prefix=None, cache_key_in_args=None, only_read=False, timeout=0):
        pass

