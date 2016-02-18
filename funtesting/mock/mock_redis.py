# -*- coding: utf8 -*-
"""
    funtesting.mock_redis
    ~~~~~~~~~~~~~~~~~~~~~

    Using `fakeredis` to mock `redis`.
"""

import fakeredis
from mock import patch


def mock_redis():
    """Mock `redis.Redis` and `redis.StrictRedis` using
    `fakeredis.FakeRedis` and `fakeredis.FakeStrictRedis`.
    """
    redis_patch = patch("redis.Redis", fakeredis.FakeRedis)
    redis_patch.start()

    strictredis_patch = patch("redis.StrictRedis", fakeredis.FakeStrictRedis)
    strictredis_patch.start()
