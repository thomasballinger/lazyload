import sys

class LazyModule(object):
    """Lazily import a module with minimal side effects"""
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, attr):
        if not self.module:
            del sys.modules[self.module_name]
            self.module = __import__(self.module_name)

            # future imports will get the real module
            sys.modules[self.module_name] = __import__(self.module_name)

        return getattr(self.module, attr)


def make_lazy(module_name):
    sys.modules[module_name] = LazyModule(module_name)
