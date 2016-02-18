# -*- coding: utf8 -*-
"""
    tests.test_manager
    ~~~~~~~~~~~~~~~~~~

    TestManager
"""

import unittest
from mock import MagicMock


class TestManager(unittest.TestCase):
    """Uniitest testcase for `TestManager`."""

    def setUp(self):
        """Setup tests."""
        from funtesting.manager import Manager
        self.manager = Manager()
        self.manager.enabled = True

    def test_options(self):
        """Test method `TestManager.options`."""
        parser = MagicMock()
        env = {}
        self.manager.options(parser, env)
        self.assertEqual(parser.add_option.call_count, 1)
