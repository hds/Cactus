#coding:utf-8
import unittest
import tempfile
import shutil
import os
from cactus.config import Config

import django.conf

from cactus.utils.packaging import bootstrap


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.path = os.path.join(self.test_dir, 'test')
        self.clear_django_settings()

        bootstrap(self.path)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def clear_django_settings(self):
        django.conf.settings._wrapped = django.conf.empty

    def assertFileExists(self, path):
        """
        Check that a file at path exists.
        """
        try:
            open(path)
        except IOError:
            self.fail("File does not exist: {0}".format(path))


class SiteTest(BaseTest):
    def setUp(self):
        super(SiteTest, self).setUp()

        self.config_path = os.path.join(self.path, 'config.json')
        self.conf = Config(self.config_path)
        self.conf.set('site-url', 'http://example.com/')
        self.conf.write()