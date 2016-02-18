# -*- coding: utf8 -*-
"""
    funtesting.manage
    ~~~~~~~~~~~~~~~~~

    Plugins' manager.
"""


from nose.plugins import Plugin

from funtesting import mock


class Manager(Plugin):
    """Funtesting manager."""

    def options(self, parser, env):
        """Register options.

        :param optparse.OptionParser parser: OptionParser instance
        :param dict env: Environment variables
        """
        parser.add_option("--mock-redis",
                          action="store_true",
                          dest="mock_redis",
                          default=env.get("MOCK_REDIS"),
                          help="Mock redis")

    def configure(self, options, conf):
        """Configure."""
        super(Manager, self).configure(options, conf)
        # If the plugin is enabled.
        if self.enabled:
            self.mock_redis = options.mock_redis

    def begin(self):
        """Setup needed before testing begins."""
        if self.mock_redis:
            mock.mock_redis()
