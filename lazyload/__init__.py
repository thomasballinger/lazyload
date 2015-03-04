import sys
from types import ModuleType


class _LazyModuleMarker(object):
    pass


def make_lazy(module_name):
    sys_modules = sys.modules  # cache in the locals
    module = None

    class LazyModule(_LazyModuleMarker):
        """Lazily import a module with minimal side effects"""
        def __mro__(self):
            """Override the __mro__ to fool `isinstance`"""
            return (LazyModule, ModuleType)

        def __getattribute__(self, attr):
            """Override __getattribute__ to hide the implementation details"""
            nonlocal module
            if module is None:
                del sys_modules[module_name]
                module = __import__(module_name)

                sys_modules[module_name] = __import__(module_name)

            return getattr(module, attr)

    sys_modules[module_name] = LazyModule()
