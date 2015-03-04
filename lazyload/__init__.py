import sys
from types import ModuleType


class _LazyModuleMarker(object):
    """
    A marker to indicate a LazyModule type.
    Allows us to check module's with `isinstance(mod, _LazyModuleMarker)`
    to know if the module is lazy.
    """
    pass


def make_lazy(module_path):
    """
    Mark that this module should not be imported until an
    attribute is needed off of it.
    """
    sys_modules = sys.modules  # cache in the locals

    # store our 'instance' data in the closure.
    module = [None]  # list because Python 2 closures are read-only

    class LazyModule(_LazyModuleMarker):
        """
        A standin for a module to prevent it from being imported
        """
        def __mro__(self):
            """
            Override the __mro__ to fool `isinstance`.
            """
            # We don't use direct subclassing because `ModuleType` has an
            # incompatible metaclass base with object (they are both in c)
            # and we are overridding __getattribute__.
            # By putting a __mro__ method here, we can pass `isinstance`
            # checks without ever invoking our __getattribute__ function.
            return (LazyModule, ModuleType)

        def __getattribute__(self, attr):
            """
            Override __getattribute__ to hide the implementation details.
            """
            if module[0] is None:
                del sys_modules[module_path]
                module[0] = __import__(module_path)

                sys_modules[module_path] = __import__(module_path)

            return getattr(module[0], attr)

    sys_modules[module_path] = LazyModule()
