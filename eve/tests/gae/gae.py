import os
from flask.ext.testing import TestCase
from eve import Eve


class GAETests(TestCase):
    def create_app(self):
        SETTINGS = 'settings.py'
        settings_file = os.path.join(os.path.split(__file__)[0], SETTINGS)
        self.app = Eve(settings=settings_file, data=None)
        return self.app

    def test_ok(self):
        pass

