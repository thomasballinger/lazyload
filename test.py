import sys
from types import ModuleType
import unittest

from lazyload import make_lazy, _LazyModuleMarker


class LazyLoadTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modname = 'abc'

    def tearDown(self):
        sys.modules.pop(self.modname, None)  # remove from the modules.

    def test_adds_to_modules(self):
        """
        Tests that `make_lazy` adds an entry to `sys.modules`.
        """
        make_lazy(self.modname)
        abc = sys.modules.get(self.modname)
        self.assertIsNotNone(
            abc,
            'make_lazy failed to add {mod} to the system modules'.format(
                mod=self.modname,
            ),
        )
        self.assertIsInstance(
            abc, ModuleType, '{mod} is not a module'.format(mod=self.modname),
        )

    def test_is_lazy_module(self):
        """
        Tests that `make_lazy` adds lazy module objects
        instead of strict module objects.
        """
        make_lazy(self.modname)
        mod = __import__(self.modname)

        self.assertIsInstance(mod, _LazyModuleMarker)

    def test_no_leaking_attributes(self):
        """
        Tests that consumers of the objects added by `make_lazy`
        cannot accidently get the attributes off of the proxy.
        """
        mod = __import__(self.modname)
        self.assertNotIsInstance(
            mod,
            _LazyModuleMarker,
            '{mod} should not be lazy yet'.format(mod=self.modname),
        )
        self.assertFalse(
            hasattr(mod, '__mro__'),
            'The module object actually has an __mro__, pick another'
            ' attribute to test',
        )

        make_lazy(self.modname)
        mod = __import__(self.modname)
        self.assertIsInstance(
            mod,
            _LazyModuleMarker,
            '{mod} should now be lazy'.format(mod=self.modname),
        )
        self.assertFalse(
            hasattr(mod, '__mro__'),
            '{mod} should not leak the abstraction by exposing __mro__'.format(
                mod=self.modname,
            ),
        )


if __name__ == '__main__':
    unittest.TextTestRunner().run(
        unittest.defaultTestLoader.loadTestsFromTestCase(LazyLoadTestCase),
    )
