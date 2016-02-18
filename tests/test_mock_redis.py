# -*- coding: utf8 -*-
"""
    tests.test_mock_redis
    ~~~~~~~~~~~~~~~~~~~~~

    TestMockRedis
"""

import unittest


class TestMockRedis(unittest.TestCase):
    """Uniitest testcase for `TestMockRedis`."""

    def test_mock_redis(self):
        """Test mock redis."""
        from fakeredis import FakeRedis, FakeStrictRedis
        from funtesting.mock import mock_redis
        mock_redis()
        from redis import Redis, StrictRedis
        cli = Redis()
        self.assertTrue(isinstance(cli, FakeRedis))
        cli = StrictRedis()
        self.assertTrue(isinstance(cli, FakeStrictRedis))
