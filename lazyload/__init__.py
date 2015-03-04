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
    module = None  # store our 'instance' data in the closure.

    class LazyModule(_LazyModuleMarker):
        """
        Lazily import a module with minimal side effects.
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
            nonlocal module
            if module is None:
                del sys_modules[module_path]
                module = __import__(module_path)

                sys_modules[module_path] = __import__(module_path)

            return getattr(module, attr)

    sys_modules[module_path] = LazyModule()
