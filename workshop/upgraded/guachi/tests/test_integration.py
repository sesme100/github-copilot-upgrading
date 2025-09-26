from os import path, remove, mkdir
import unittest
from guachi import ConfigMapper

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.mapped_options = {
            'guachi.db.host': 'db_host',
            'guachi.db.port': 'db_port',
            'guachi.web.host': 'web_host',
            'guachi.web.port': 'web_port',
        }
        self.mapped_defaults = {
            'db_host': 'localhost',
            'db_port': 27017,
            'web_host': 'localhost',
            'web_port': '8080',
        }
        # 테스트 간 DB 파일 초기화
        try:
            if path.exists('/tmp/guachi/guachi.db'):
                remove('/tmp/guachi/guachi.db')
        except Exception:
            pass
        try:
            if not path.exists('/tmp/guachi'):
                mkdir('/tmp/guachi')
        except Exception:
            pass

    def tearDown(self):
        # 테스트 후 DB 파일 삭제
        try:
            if path.exists('/tmp/guachi/guachi.db'):
                remove('/tmp/guachi/guachi.db')
        except Exception:
            pass

    def test_access_mapped_configs_empty_dict(self):
        foo = ConfigMapper('/tmp/guachi')
        foo.set_ini_options(self.mapped_options)
        foo.set_default_options(self.mapped_defaults)
        foo.set_config({})
        self.assertEqual(foo(), {})
        self.assertEqual(foo.path, '/tmp/guachi/guachi.db')
        self.assertEqual(foo.get_ini_options(), {})
        self.assertEqual(foo.get_default_options(), {})
        self.assertEqual(foo.get_dict_config(), self.mapped_defaults)
        self.assertEqual(foo.stored_config(), {})
        self.assertTrue(foo.integrity_check())

    def test_access_mapped_configs_dict(self):
        foo = ConfigMapper('/tmp/guachi')
        foo.set_ini_options(self.mapped_options)
        foo.set_default_options(self.mapped_defaults)
        foo.set_config({'db_host': 'example.com', 'db_port': 0})
        self.assertEqual(foo(), {})
        self.assertEqual(foo.path, '/tmp/guachi/guachi.db')
        self.assertEqual(foo.get_ini_options(), {})
        self.assertEqual(foo.get_default_options(), {})
        self.assertEqual(foo.get_dict_config(), {
            'web_port': '8080',
            'web_host': 'localhost',
            'db_host': 'example.com',
            'db_port': 0
        })
        self.assertEqual(foo.stored_config(), {})
        self.assertTrue(foo.integrity_check())
